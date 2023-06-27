# %%

import base64
import lengthext
d = {"a": "b", "a": "c"}
d

# %%


# %%

payload = base64.b64decode(
    "bmFtZT1hfGFuaW1hbD1ifGFkbWluPWZhbHNlfG1hYz0wYTM2NjI2ZDFhOWU5YWY0MTU1ZGQ4MjJlZWQ5ZWVkYzIyNDA4Mjdl")
msg, token = payload.split(b"|mac=")
msg, token

# %%
# token = SHA(key + data) = SHA(key + name=a|animal=b|admin=false)
new_msg = msg + b"|admin=true"
new_msg

# %%
sha = lengthext.new("sha1")
message = sha.extend("|admin=true", msg, 32, token.decode(
    "latin1"), raw=True).encode("latin1")
mac = sha.hexdigest()

# %%
token = message + b"|mac=" + mac.encode("latin1")
base64.b64encode(token).decode("latin1")

