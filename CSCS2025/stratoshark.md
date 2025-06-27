# User

```
/etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```


# SSH related things

```bash
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDROHNw4IF2tSGWGJlZjvvieP0Sx9QxkqKwpI6ercuT
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILDI13bYIJZmIQ3RD2K0/Itj7n3ozi/mo1zVdCrRAZOQ
ssh-connection
ssh-connection
ssh-ed25519
ssh-ed25519
ssh-ed25519
ssh-ed25519
ssh-ed25519
ssh-connection
ssh-connection
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDROHNw4IF2tSGWGJlZjvvieP0Sx9QxkqKwpI6ercuT
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILDI13bYIJZmIQ3RD2K0/Itj7n3ozi/mo1zVdCrRAZOQ
ssh-connection
ssh-connection
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDROHNw4IF2tSGWGJlZjvvieP0Sx9QxkqKwpI6ercuT
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILDI13bYIJZmIQ3RD2K0/Itj7n3ozi/mo1zVdCrRAZOQ
ssh-connection
ssh-connection
```

# How do SSH files look like

```bash
❯ ssh-keygen
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/bluk/.ssh/id_ed25519): /Users/bluk/Developer/ctf/CSCS2025/assets/stratoshark/testkey
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/bluk/Developer/ctf/CSCS2025/assets/stratoshark/testkey
Your public key has been saved in /Users/bluk/Developer/ctf/CSCS2025/assets/stratoshark/testkey.pub
The key fingerprint is:
SHA256:ulpewhUUi7yKJ+jmgBK2Se1o49x6Jg+oR47Z4guiMCs bluk@Satan.local
The key's randomart image is:
+--[ED25519 256]--+
|        o.       |
|     . o .       |
|      o o        |
|  .    . .       |
|.o .  . S        |
|=o*. o o         |
|@&o.o = .        |
|E=B= o +         |
|O@Bo..o          |
+----[SHA256]-----+
❯ ls
testkey       testkey.pub   traces.pcapng
❯ cat testkey*
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACCOdMAHTeWWiN1RlYdZjG5gLDhfXTCYZKtzjtrttJAMGAAAAJjCIbJFwiGy
RQAAAAtzc2gtZWQyNTUxOQAAACCOdMAHTeWWiN1RlYdZjG5gLDhfXTCYZKtzjtrttJAMGA
AAAEBDnHiK4Ow1DkUypJnPqYHzatWb4THf1syHZ2db88GDmY50wAdN5ZaI3VGVh1mMbmAs
OF9dMJhkq3OO2u20kAwYAAAAEGJsdWtAU2F0YW4ubG9jYWwBAgMEBQ==
-----END OPENSSH PRIVATE KEY-----
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII50wAdN5ZaI3VGVh1mMbmAsOF9dMJhkq3OO2u20kAwY bluk@Satan.local

```

With `strings` we find

```bash
/etc/ssh/ssh_host_rsa_key
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAA
/etc/ssh/ssh_host_rsa_key
/etc/ssh/ssh_host_rsa_key
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAA
/etc/ssh/ssh_host_rsa_key.pub
/etc/ssh/ssh_host_rsa_key.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDROHNw4IF2tSGWGJlZjvvieP0Sx9QxkqKwpI6ercuT
/etc/ssh/ssh_host_ecdsa_key
/etc/ssh/ssh_host_ecdsa_key
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAA
/etc/ssh/ssh_host_ecdsa_key
/etc/ssh/ssh_host_ecdsa_key
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAA
/etc/ssh/ssh_host_ecdsa_key.pub
/etc/ssh/ssh_host_ecdsa_key.pub
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFxBCHfU
/etc/ssh/ssh_host_ed25519_key
/etc/ssh/ssh_host_ed25519_key
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAA
/etc/ssh/ssh_host_ed25519_key
/etc/ssh/ssh_host_ed25519_key
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAA
/etc/ssh/ssh_host_ed25519_key.pub
/etc/ssh/ssh_host_ed25519_key.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILDI13bYIJZmIQ3RD2K0/Itj7n3ozi/mo1zVdCrRAZOQ
```

```
❯ nmap -Pn -p 22 --script ssh-auth-methods 168.119.249.32
Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-01 23:27 EDT
Nmap scan report for static.32.249.119.168.clients.your-server.de (168.119.249.32)
Host is up (0.13s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-auth-methods: 
|   Supported authentication methods: 
|_    publickey

Nmap done: 1 IP address (1 host up) scanned in 1.14 seconds
```

connecting results into this public key WHICH IS DIFFERENT

´´´
168.119.249.32 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIb5uT345479mBsq82bZhCa3dWJCCr5N31wP3eagP14s
```

data: 2994af5f84657fa55e3f0681be096413f6db2dd7ddfa742ac602413c37011c4a7da44466f2c4f910

data: 2994af5f84657fa55e3f0681be096413f6db2dd7ddfa742ac602413c37011c4a7da44466f2c4f910

name: /root/so_injection/example_so/target/debug/libexample_so.so
