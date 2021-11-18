password = "fc fd ea c0 ba ec e8 fd fb bd f7 be ef b9 fb f6 bd c0 ba b9 f7 e8 f2 fd e8 f2 fc".replace(" ","")

pw_bytes = bytearray.fromhex(password)

for i in range(len(pw_bytes)):
    pw_bytes[i] = (pw_bytes[i] + 119) % 256

print(str(pw_bytes))

