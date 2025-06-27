#!/usr/bin/env python3
import sys
from base64 import b64encode
from hashlib import md5
from zlib import crc32

with open(sys.argv[1],"rb") as f:
    x1 = f.read()
    
with open(sys.argv[2],"rb") as f:
    x2 = f.read()

h1 = md5(x1).digest()
h2 = md5(x2).digest()

if not h1 == h2:
    print("bug")
    print(sys.argv[1],"->",h1.hex())
    print(sys.argv[2],"->",h2.hex())
    exit()

h1 = crc32(h1 + x1).to_bytes(4, "little")
h2 = crc32(h2 + x2).to_bytes(4, "little")

if h1 == h2:
    print("Collision: ",b64encode(x1)," - ",b64encode(x2),sep="")
else:
    print("1")