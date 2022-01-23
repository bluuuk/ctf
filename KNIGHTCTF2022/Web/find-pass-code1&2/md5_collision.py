import hashlib

PREFIX = "0e"
c = 840922711

"""

By looking at the source we can see that they only test against the inputs

0e{215962017, 730083352, 807097110, 840922711}

So we start searching after 840922711 for a new collision

=> 0e1137126905 0e291659922323405260514745084877
"""

while True:
    hash = hashlib.md5(bytes(PREFIX + str(c),"ASCII")).digest().hex()
    if hash.startswith(PREFIX) and hash[2:].isdigit():
        print(PREFIX + str(c))
        break
    else:
        c += 1

res = PREFIX + str(c)

print(res,hashlib.md5(bytes(res,"ASCII")).digest().hex())