- Use `a` when using wordlists
- md5 maps to `-m 0`

```bash
❯ hashcat -a 0 -m 0 chall1.hashes rockyou.txt
hashcat (v6.2.6) starting

* Device #2: Apple's OpenCL drivers (GPU) are known to be unreliable.
             You have been warned.

METAL API (Metal 368.12)
========================
* Device #1: Apple M1 Pro, 5408/10922 MB, 14MCU

OpenCL API (OpenCL 1.2 (Apr 18 2025 21:46:03)) - Platform #1 [Apple]
====================================================================
* Device #2: Apple M1 Pro, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 3 digests; 3 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 100c

Host memory required for this attack: 245 MB

Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

53e182cbd4daa6680f1a7c7b85eba802:cookiezz                 
1853572d1b6ae6f644718a6b6df835f9:sauron82                 
1bfcbffaf03174f022225a62ddf025a8:m00nl!ght                
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: chall1.hashes
Time.Started.....: Tue Jul 15 00:35:01 2025 (1 sec)
Time.Estimated...: Tue Jul 15 00:35:02 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 25894.4 kH/s (7.39ms) @ Accel:1024 Loops:1 Thr:64 Vec:1
Recovered........: 3/3 (100.00%) Digests (total), 3/3 (100.00%) Digests (new)
Progress.........: 6422528/14344385 (44.77%)
Rejected.........: 0/6422528 (0.00%)
Restore.Point....: 5505024/14344385 (38.38%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: mintesimal -> kybignasty
Hardware.Mon.SMC.: Fan0: 0%, Fan1: 0%
Hardware.Mon.#1..: Util: 46%

Started: Tue Jul 15 00:34:54 2025
Stopped: Tue Jul 15 00:35:03 2025
```


