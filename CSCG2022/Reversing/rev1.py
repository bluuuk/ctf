#!/usr/bin/python3

hiddenflag = "".join([
    "Welcome to your 1st Reverse-Engineering Challenge. Take a Decompiler of your choice and check out the source code. :)".split(" ")[8],
    "s_are_",
    "".join(['y','l','l','a','e','r'][::-1]),
])
 
msg = "\x5F\x70\x6F\x77\x65\x72\x66\x75\x6C\x6C\x21"

print(f"CSCG{{{hiddenflag+msg}}}")