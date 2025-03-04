#%% their part
def genkeys(n):
    keys = [os.urandom(5) for _ in range(n)]
    return keys

def encrypt(keys, flag):
    for key in keys:
        flag = bytes([a ^ b for a, b in zip(flag, key * (len(flag)+5//5)
        )])
    return flag

# [byte[5], byte[5], byte[5], byte[5], byte[5] ,...]
keys = genkeys(1955) # with this many keys, this is totally secure

print(encrypt(keys,flag).hex())
# # however, the main key is the xor of all keys, so encrypt is like:
# def encrypt(keys, flag):
#     key = XOR key_i for key_i in genkeys(1955)
#     return bytes([a ^ b for a, b in zip(flag, key * (len(flag)+5//5))])
#
# flag = XOR_i{0}^{1955}(flag ^ key[i])
# flag = XOR_i{1}^{1955}(flag) ^ XOR_i{1}^{1955}( key[i])
# flag = flag ^ XOR_i{1}^{1955}(key[i])


# We can verify it via:
# def encrypt2(keys, flag):
#     full_key = keys[0]
#     for key in keys[1:]:
#         full_key = bytes([a ^ b for a, b in zip(full_key,key)])

#     flag = bytes([a ^ b for a, b in zip(flag, full_key * (len(flag)+5//5))])
#     return flag

# keys = genkeys(1955) # with this many keys, this is totally secure
# assert encrypt(keys, flag).hex() == encrypt2(keys, flag).hex()




#%%

import os
import string

flag = bytes.fromhex(open("output.txt", "r").read())
print(len(flag))

#%% solve 

key = bytes([
    known ^ cipher for known,cipher in 
    zip(bytes("HTB{",encoding="utf8"),flag)
])


for test in range(255):
    tmpkey = key + bytes([test])
    res = bytes([a ^ b for a, b in zip(flag, tmpkey * (len(flag)+5//5))])

    compare = string.ascii_letters + string.digits + string.punctuation

    try:
        decoded = res.decode(encoding="ASCII")
    except:
        continue
    if all((char in compare) for char in decoded):
        print(decoded) 

# => HTB{d0_w3_r34lly_n33d_th1s_m4ny_c4r_k3y5_f0r_4_s1lly_t1me_m4ch1n3??}

