# Meet in the middle attack

- Encrypt a selected plaintext
- Decrypt the corresponding ciphertext

Let $x = Enc(plaintext)$ and $y = Dec(ciphertext)$. If $x=y$, we have two possible keys. Then we test the total encryption.

Encrypted Flag:

```
2e9e5bf227e474ae67605dab1f1e915edd251129ad07389ff7e001cc1ecee8295de440ce95bdf0f049e29801108e04accbd1d1d5895f6c45e08a2fc78172d7c6f2c0ab7eec18cf265b6c7f831cc4ef2f922de3f946ac43f7a4dad6b9a81fecce
```

We know select our plaintext, which will padded by the encryption oracle. But we can just use the first block due to ECB.

```
00000000000000000000000000000000
```
(32 BYTES)

which results into the payload

```
{"pt": "3030303030303030303030303030303030303030303030303030303030303030"}
```

In the ciphertext, we can see that the first two blocks are repeated because of ECB.

```
ccd972d05bca994ffd3e4b8d54ed77c9ccd972d05bca994ffd3e4b8d54ed77c986d073696cd4c29689aaebc29ac0084f
```

(48 BYTES)