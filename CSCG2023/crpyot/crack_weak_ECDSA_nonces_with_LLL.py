#!/usr/bin/env python
# Author Dario Clavijo 2020
# based on previous work:
# https://blog.trailofbits.com/2020/06/11/ecdsa-handle-with-care/
# https://www.youtube.com/watch?v=6ssTlSSIJQE


#%%
import sys
import ecdsa
import random
from sage.all import *
import gmpy2

# order is from secp256k1 curve it can be used any other.
order = int(ecdsa.BRAINPOOLP256r1.order)

def modular_inv(a,b):
  return int(gmpy2.invert(a,b))

# def load_csv(filename, limit = None):
#   msgs = []
#   sigs = []
#   pubs = []
#   fp = open(filename)
#   n=0
#   if limit == None:
#     limit = -1
#   for line in fp:
#     if (limit == -1) or (n < limit):
#       l = line.rstrip().split(",")
#       tx,R,S,Z,pub = l
#       msgs.append(int(Z,16))
#       sigs.append((int(R,16),int(S,16)))
#       pubs.append(pub)
#       n+=1
#   return msgs,sigs,pubs


def make_matrix(msgs, sigs, B):
  m = len(msgs)
  sys.stderr.write("Using: %d sigs...\n" % m)
  matrix = Matrix(QQ, m + 2, m + 2)

  msgn, rn, sn = [msgs[-1], sigs[-1][0], sigs[-1][1]]
  rnsn_inv = rn * modular_inv(sn, order)
  mnsn_inv = msgn * modular_inv(sn, order)

  for i in range(0,m):
    matrix[i,i] = order

  for i in range(0,m):
    x0=(sigs[i][0] * modular_inv(sigs[i][1], order)) - rnsn_inv
    x1=(msgs[i] * modular_inv(sigs[i][1], order)) - mnsn_inv
    matrix[m+0,i] = x0
    matrix[m+1,i] = x1
 
  matrix[m+0,i+1] = (int(2**B) / order)
  matrix[m+0,i+2] = 0
  matrix[m+1,i+1] = 0
  matrix[m+1,i+2] = 2**B

  return matrix


def privkeys_from_reduced_matrix(msgs, sigs, matrix):
  keys=[]
  msgn, rn, sn = [msgs[-1], sigs[-1][0], sigs[-1][1]]
  for row in matrix:
    potential_nonce_diff = row[0]
    potential_priv_key = (sn * msgs[0]) - (sigs[0][1] * msgn) - (sigs[0][1] * sn * potential_nonce_diff)
    try:
      potential_priv_key *= modular_inv((rn * sigs[0][1]) - (sigs[0][0] * sn), order)
      key = potential_priv_key % order
      if key not in keys:
        keys.append(key)
    except Exception as e:
      sys.stderr.write(str(e)+"\n")
      pass
  return keys

#%% 
import ecdsa
import ecdsa.curves
import os
from hashlib import shake_128


BANNER = """
WELCOME to the demo version of sig1337nature.
Our signature signing is faster than anyone!

In our demo you can request up to 69 signatures!

To show how certain we are in our construction, we even included a bug bounty program.
"""

FLAG = "FLAG"


def efficient_k(msg):
    # Make semi-deterministic to not exhaust the entropy pool too fast
    return int.from_bytes(
        shake_128(msg).digest(16) + os.urandom(16),
        "big"
    )

def sign_msg(priv_key,msg):
    if b"flag" in msg:
        print("No way, jose!")
        return

    sig = priv_key.sign(msg, k=efficient_k(msg))

    print("Signature (hex):", sig.hex())


#%% 

from collections import namedtuple
from ecdsa import util
Signature = namedtuple("signature",("r","s"))
privkey = ecdsa.SigningKey.generate(curve=ecdsa.curves.BRAINPOOLP256r1)
pubkey = privkey.get_verifying_key()
inital_msg = b"0"
msg = int.from_bytes(inital_msg,"big")
B = 2**128
run_mode = "LLL"

def sign():
    sig = privkey.sign(inital_msg, k=efficient_k(inital_msg))
    r,s = util.sigdecode_string(sig,ecdsa.curves.BRAINPOOLP256r1.order)
    return r,s

msgs,sigs = [],[]

for _ in range(10):
  msgs.append(msg)
  sigs.append(sign())

matrix = make_matrix(msgs, sigs, B)

if run_mode == "LLL":
  new_matrix = matrix.LLL(early_red=True, use_siegel=True)
  keys = privkeys_from_reduced_matrix(msgs, sigs, new_matrix)
else:
  new_matrix = matrix.BKZ(early_red=True, use_siegel=True)
  keys = privkeys_from_reduced_matrix(msgs, sigs, new_matrix)

print(keys)

privkey.privkey.__dict__["secret_multiplier"]

# %%
