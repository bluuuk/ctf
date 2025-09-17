1. Transalte the `wasm.wat` hand by hand into c pseudocode. I rechecked transpiling errors with chatGPT and it accedentially told me this is unicode conversion.

```c
//(func $encode (export "encode") (param $src i32) (param $dest i32)
void encode(src *int32[], dest *uint8[]){
    src_index, dest_index i32;

    // a list of unicode code points
    src_index = 0
    // write bytes into dest to encode unicode cp's 
    dest_index = 0

    while(src[src_index] != 0){
        // why 0x1F4C0
        dest_index += encode_codepoint(src[src_index] + 0x1F4C0, dest + dest_index)
        src_index += 1
    }
    dest[dest_index] = 0
}
```

```c
i32 encode_codepoint(codepoint i32, bytebuffer* uint8[]){
    last,middle i32;

    if (codepoint < 0x80){ // U+0000 to U+007F aka 1 byte : 0b10000000(0x80) -> 0xxxxxxx
        bytebuffer[0] = codepoint
        return 1
    }

    last = (codepoint & 0x3F) + 0x80
    if(codepoint < 0x800){ // U+0080 to U+07FF aka 2 byte : 0b00111111(0x3F) 0b11000000(0xC0) -> 110xxxxx 10xxxxxx
        bytebuffer[1] = last
        bytebuffer[0] = (codepoint >> 6) + 0xC0
        return 2
    }

    middle = ((codepoint >> 6) & 0x3F ) + 0x80
    if(codepoint < 0x010000){// U+0000 to U+007F aka 1 byte :'0b10000000' -> 1110xxxx 10xxxxxx 10xxxxxx
      bytebuffer[0] = (codepoint >> 12) + 0xE0
      bytebuffer[1] = middle
      bytebuffer[2] = last
      return 3
    }
   
   // U+0000 to U+007F aka 1 byte :'0b10000000' -> 0xxxxxxx
    return encode_codepoint(0xFFFD, bytebuffer)
}
```

- As we can see, the code point with 4 bytes is not represented
- The script below is called from JS

```js
async function go() {
  const src = 0;
  const dst = 0x100;

  const memory = new WebAssembly.Memory({initial: 1, maximum: 1});
  const wasm = await WebAssembly.instantiateStreaming(fetch("wasm.wasm"), {js: {mem: memory}});
  
  // RṁpNåḞS¶
  const input = new Uint8Array(await fetch("input.txt").then(e => e.arrayBuffer()));
  new Uint8Array(memory.buffer, src, input.byteLength).set(input);
  new Uint8Array(memory.buffer, src + input.byteLength, 1).set([0]);
  // dest_index += encode_codepoint(src[src_index] + 0x1F4C0, dest + dest_index)
  wasm.instance.exports.encode(src, dst);
  
  const view = new DataView(memory.buffer);
  var i;
  for (i = dst; view.getUint8(i) !== 0; i++) {}

  const flag = await fetch("/flag.txt", {method: "POST", headers: {"Content-Type": "application/octet-stream"}, body: memory.buffer.slice(dst, i)}).then(e => e.text());

  document.getElementById("output").value = flag;
}
```

- So this script fails for emoji input, which are usually 4 byte. 
  - Why does `encode()` call `encode_codepoint()` with `0x1F4C0`? ChatGPT is expeptionally good at understanding unicode, like telling me that the hex value is `📀`
  - Therefore, the script receives input.txt (`RṁpNåḞS¶`) and encodes this into the byte representation
  - I tried with python, but it somehow failed:

```python
In [32]: "".join([chr(ord(char) + ord('📀')) for char in "RṁpNåḞS¶"]).encode("utf-8")
Out[32]: b'\xf0\x9f\x94\x92\xf0\xa1\x8c\x81\xf0\x9f\x94\xb0\xf0\x9f\x94\x8e\xf0\x9f\x96\xa5\xf0\xa1\x8b\x9e\xf0\x9f\x94\x93\xf0\x9f\x95\xb6'

In [33]: b64encode(_)
Out[33]: b'8J+UkvChjIHwn5Sw8J+UjvCflqXwoYue8J+Uk/CflbY='
```

However, it does not correspond to the js version:

```javascript
(async () => {
  const input = new Uint8Array(await fetch("input.txt").then(e => e.arrayBuffer()));
  // This is the correct Unicode string you want to send
  const codepoints = Array.from(input)
  .map(b => 0x1F4C0 + b);

  // Step 3: Convert codepoints to a string
  const str = String.fromCodePoint(...codepoints);
  console.log(new Uint8Array(codepoints).toBase64())
  console.log(str)

  // Step 4: Encode as UTF-8
  const encoder = new TextEncoder();
  const utf8 = encoder.encode(str); // Uint8Array of UTF-8 bytes

  // Send to /flag.txt
  const response = await fetch("/flag.txt", {
    method: "POST",
    headers: {
      "Content-Type": "application/octet-stream"
    },
    body: utf8
  });

  const flag = await response.text();
  console.log(flag);
  document.getElementById("output").value = flag;
})();
```

which returns `EnUwDqVwE3Y=` as the right payload. I think it is due to the input array data, which got shifted around while copying. => FLAG{we_have_assembly_in_the_web}
