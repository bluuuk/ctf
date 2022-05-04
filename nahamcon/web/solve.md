# Solve

Break the regex by supplying a username and settings for the regex

```python
flag = open("flag.txt").read()
users = open("users.txt").read()

users += flag

...

results = re.findall(r"[A-Z][a-z]*?" + name + r"[a-z]*?\n", users, setting)
```

We know that the flag always has the format `flag{...}` such that it starts with a lower case char. Therefore, we use the setting `re.IGNORECASE` which translates `[A-Z]` to `[a-z]` according to the [docs](https://docs.python.org/3/library/re.html). The final name is `.*` to match everything.