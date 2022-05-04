"""
import random

flag = open('flag.txt', 'r').read()
ct = ''
k = random.randrange(0,0xFFFD)
for c in flag:
    ct += chr((ord(c) + k) % 0xFFFD)

open('out', 'w').write(ct)
"""

#%%

# simple vigenere cipher where we know the key because of known plaintext

mod = 0xFFFD

with open("out","r") as f:
    data = f.read()

    key = ord(data[0]) - ord("f") % mod 

    flag = "".join(
        chr((ord(x) - key) % mod) for x in data
    )

    print(flag)
