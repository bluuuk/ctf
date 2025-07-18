# 🧠 Reverse‑engineering an Android app with Chaquopy

## 1. Android app setup
- The app uses **[Chaquopy](https://github.com/chaquo/chaquopy)** to run Python code on Android 📱.
- Python files are packaged inside APK ZIP containers and come in **compiled `.pyc` form**.
- You discovered a hidden function `get_secret_reward`.

## 2. Local limitations
- On your Mac, you can't install the **Toga (UI)** dependency — so you can’t just import all modules normally.

## 3. Inspecting the `.pyc` file with `dis`
I tried to simply dissassemble it (other packages do not support python 3.12):

```python
import dis
dis.dis(open("app.pyc","rb").read())
```

But got:

```
IndexError: list index out of range
```

This happens because `.dis` expects a **code object**, not raw `.pyc` bytes with a header.

## 4. Fixed disassembly approach

```python
import marshal, dis

with open("app.pyc", "rb") as f:
    f.seek(16)                       # Skip 16‑byte header (magic+flags+timestamp) for Python 3.7+.
    code = marshal.load(f)           # Extract the code object
dis.dis(code)                        # Disassemble safely
```

- This works around the header and exposes the bytecode logic.

## 5. Magic number verification

- The `.pyc` header starts with: `\xcb\r\r\n`.
- That corresponds to **Python 3.12** (magic number 3531) — which matches your local Python 3.12.8 interpreter.

## 6. Accessing the secret function

```
Disassembly of <code object get_secret_reward at 0xffffac3b4c00, file "app.py", line 125>:
125           0 RESUME                   0

126           2 LOAD_CONST               1 ('eJzzMXb0rvYqLS6JN4kPNynKjQ8tiHfOMMnJqQUAeHcJQA==')
              4 STORE_FAST               0 (compressed_flag)

127           6 NOP

128           8 LOAD_GLOBAL              1 (NULL + base64)
             18 LOAD_ATTR                2 (b64decode)
             38 LOAD_FAST                0 (compressed_flag)
             40 CALL                     1
             48 STORE_FAST               1 (decoded)

129          50 LOAD_GLOBAL              5 (NULL + zlib)
             60 LOAD_ATTR                6 (decompress)
             80 LOAD_FAST                1 (decoded)
             82 CALL                     1
             90 LOAD_ATTR                9 (NULL|self + decode)
            110 LOAD_CONST               2 ('utf-8')
            112 CALL                     1
            120 STORE_FAST               2 (flag)

130         122 LOAD_FAST                2 (flag)
            124 RETURN_VALUE
        >>  126 PUSH_EXC_INFO

131         128 POP_TOP

132         130 POP_EXCEPT
            132 RETURN_CONST             3 ('Error: Could not decode secret')
        >>  134 COPY                     3
            136 POP_EXCEPT
            138 RERAISE                  1
```

- You reversed `get_secret_reward` — which likely uses **base64 + zlib** decompression to reveal the flag.
- As a workaround during dynamic analysis, you could have:
  - **Created a dummy module** to mock missing dependencies (e.g. Toga), or
  - **Injected a fake module via `sys.modules`**, so Python can import it and let you call `get_secret_reward()` directly in REPL.

## 7. Flag decoding

Once you called `get_secret_reward()`, it returned something like:

```python
import base64, zlib
data = base64.b64decode("eJyrVkpUslJQ...")  # truncated
print(zlib.decompress(data))
```

- That plain-text output contained the flag: `FLAG{XXXX}`.

## 8. Alternative via Mock

``
>>> from unittest import mock
>>> import sys
>>> import app
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "app.py", line 1, in <module>
ModuleNotFoundError: No module named 'toga'
>>> sys.modules['toga'] = mock.MagicMock()
>>> import app
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "app.py", line 2, in <module>
ModuleNotFoundError: No module named 'toga.style'; 'toga' is not a package
>>> sys.modules['toga.style'] = mock.MagicMock()
>>> import app
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "app.py", line 3, in <module>
ModuleNotFoundError: No module named 'toga.style.pack'; 'toga.style' is not a package
>>> sys.modules['toga.style.pack'] = mock.MagicMock()
>>> import app
>>> app.get_secret_reward()
'L3AK{Just_4_W4rm_Up_Ch4ll}'
```

so, in the end, we just have to do

```python
from unittest import mock
import sys

sys.modules['toga'] = mock.MagicMock()
sys.modules['toga.style'] = mock.MagicMock()
sys.modules['toga.style.pack'] = mock.MagicMock()

import app
app.get_secret_reward()
'L3AK{Just_4_W4rm_Up_Ch4ll}'
```

---

## 🧭 TL;DR

| Step                     | Summary |
|--------------------------|---------|
| Inspect `.pyc`           | Skip header + `marshal.load()` + `dis.dis()` |
| Python version check     | `\xcb\r\r\n` → Python 3.12 |
| Fake missing imports     | Stub modules or `sys.modules` hack |
| Extract the function     | Call `get_secret_reward()` directly |
| Decode payload           | Base64 → zlib → flag string |