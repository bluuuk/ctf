If you thought rules were easy after the last challenge, think again! I've concocted more devious password mangling rules to push the limits of your cracking knowledge (and possibly your CPU...):

Use the rockyou.txt wordlist.

Flag format: L3AK{pass1_pass2_pass3}

# Password 1: Prepend 1 uppercase letter, Swap the first 2 characters, Rotate it to the right 3 times, Append a 4-digit year since 1900.

> 2a07038481b64a934495e5a91d011ecbf278aba8c5263841e1d13f73975d5397

## Prepend

```
❯ python3 -c "import string;[print('^' + x) for x in string.ascii_uppercase]" > chall3hash1upper.rule
^X
```
## Swap and rotate

```
k}}}
```

## Append

```
❯ python3 -c 'import string;[print("".join(a+b for a,b in zip("$$$$",str(x)))) for x in range(1900,2025,4)]' > chall3hash1year.rule
#1#9#9#0
```

```bash
hashcat -a 0 -r chall3hash1upper.rule -r chall3hash1swapandshift.rule -r chall3hash1year.rule -m 1400 2a07038481b64a934495e5a91d011ecbf278aba8c5263841e1d13f73975d5397 rockyou.txt
2a07038481b64a934495e5a91d011ecbf278aba8c5263841e1d13f73975d5397:er!bLigbroth1984
```

# Password 2: Lowercase the entire password. Apply a random caesar cipher shift to all the letters in the password. Then, replace each alphanumeric character with its right neighbor on the QWERTY keyboard. Finally, reverse it.

> cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25e6af2b555f6f5

## Lowercase `l`
## Casear via `sXY`
  
We can prove the observation that we always need to topologically sort:

```bash
❯ echo "sabsbc" > chall3test.rule && hashcat -a 0 -r chall3test.rule --stdout rockyou.txt | head
123456
12345
123456789
pcssword
iloveyou
princess
1234567
rockyou
12345678
ccc123 <------
❯ hashcat -a 0 --stdout rockyou.txt | head
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123 <------
❯ echo "sbcsab" > chall3test.rule && hashcat -a 0 -r chall3test.rule --stdout rockyou.txt | head
123456
12345
123456789
pbssword
iloveyou
princess
1234567
rockyou
12345678
bcc123 <------
```

However, it is not straight forward to do ceaser as there are cycles in every ceaser. However, we know that uppercases are available, so we can use 'A' as a placeholder to break the cycle. We save the first character, transform every other character and then retransform the last character.

Example

```
s12s23s34s40s01
```

This will translate everything to $4$ in a $x+1$ Ceaser cipher. To overcome this issue, we have to

- Break the cycle
- Execute in reverse order to overcome sequential processing character forwarding

As we know that the input is in lowercase, we know at least one character that is never in the input, let's say `A`. It is likely that there is always one placeholder and if not, you need to create multiple ceaser ciphers that use different placeholder to at one point hit the right input.

```
s01 s12 s23 s34 s40 
```

Let's introduce a placeholder to break the cycle `0 -> 1 -> 2 -> 3 -> 4` into `0 -> A, 1 -> 2 -> 3 -> 4, A -> 1`

```
s0A s12 s23 s34 s40 sA1 
```

However, we still process sequentially, so every $1,2,3$ will eventually become a $4$ :( Let's change that by reversing the inner order!

```
s0A s40 s34 s23 s12 sA1 
```

So, this will now do a ceaser cipher :) How do we transfrom this into an algo?

For each ceaser shift $0 \leq x \leq N$:
  1) Introduce placeholder for $x$ aka `0 -> A`
  2) Start with the highest value, here $x-1+i \mod N$ and substitute it with $x+1+i \mod N$ for each possible character $i$
  3) Exchange placeholder for $x + 1 \mod N$ aka `A -> 1`


```python
from string import ascii_lowercase as LC
with open("chall3hash2caeser.rule","w") as f:
    # ceaser with no shift via passthrough
    print(":",file=f)
    # all other ceasers
    for shift in range(1,26):
        src = list(range(26))
        dst = [(x+shift)%26 for x in range(26)]
        
        # src[0] -> dst[0]
        print(f"s{LC[src[0]]}A",end="",file=f)
        last = dst[0]
        for _ in range(26):

            print(f"s{LC[di]}{LC[si]}",end="",file=f)

        print(f"sA{LC[dst[0]]}",end="\n",file=f)
```

=> it is impossible implement this in hashcat, as we only have 31 maximum rules but a maximum of $13$ cycles where we need $13$ placeholder values => we would need $2\cdot 26$ rules :(

HOWEVER, we can just use the fact that the entire output is in lowercase, so we just use the entire uppercase space! Therefore, the idea is to apply upperspace first and then substitute in the form of `A -> a` so we do not run into any cycles as every operation is independent of others!!!! It took me quite some time to figure out to map `Upper case -> Lower case` to overcome issues

```python
from string import ascii_lowercase as LC, ascii_uppercase as UC
with open("chall3hash2caeser.rule","w") as f:
    # ceaser with no shift via passthrough
    print("l",file=f)
    # all other ceasers
    for shift in range(1,26):
        for char in range(26):
            print(f"s{UC[char]}{LC[(char + shift)%26]}",end="",file=f)
        print("",file=f)
```
Et voíla, it works

```bash
❯ hashcat -a 0 -r chall3hash2upper.rule -r chall3hash2caeser.rule test --stdout
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
defghijklmnopqrstuvwxyzabc
efghijklmnopqrstuvwxyzabcd
fghijklmnopqrstuvwxyzabcde
ghijklmnopqrstuvwxyzabcdef
hijklmnopqrstuvwxyzabcdefg
ijklmnopqrstuvwxyzabcdefgh
jklmnopqrstuvwxyzabcdefghi
klmnopqrstuvwxyzabcdefghij
lmnopqrstuvwxyzabcdefghijk
mnopqrstuvwxyzabcdefghijkl
nopqrstuvwxyzabcdefghijklm
opqrstuvwxyzabcdefghijklmn
pqrstuvwxyzabcdefghijklmno
qrstuvwxyzabcdefghijklmnop
rstuvwxyzabcdefghijklmnopq
stuvwxyzabcdefghijklmnopqr
tuvwxyzabcdefghijklmnopqrs
uvwxyzabcdefghijklmnopqrst
vwxyzabcdefghijklmnopqrstu
wxyzabcdefghijklmnopqrstuv
xyzabcdefghijklmnopqrstuvw
yzabcdefghijklmnopqrstuvwx
zabcdefghijklmnopqrstuvwxy
```

## Neighbours

```
12
23
34
45
56
67
78
89
90
0-
qw
we
er
rt
ty
yu
ui
io
op
p[
as
sd
df
fg
gh
hj
jk
kl
l;
zx
xc
cv
vb
bn
nm
m,
```

which yields ```s12s23s34s45s56s67s78s89s90s0_sqwswesersrtstysyusuisiosopsp[sasssdsdfsfgsghshjsjksklsl;szxsxcscvsvbsbnsnmsm,```

However, this results into always the same character as a sequentail transformation, so we have to reverse it, aka sort it topologically:

```python
from itertools import batched
data = open("chall3hash2qwerty.rule","r").read()
with open("chall3hash2qwertyfixed.rule","w") as f:
    for _,a,b in list(batched(data,3))[::-1]:
        f.write(f"s{a}{b}")
```

We also note that 

> With hashcat, the number of functions of a single rule line and the overall number of functions of multi-rules is limited to 31.

Such that we have to split our rule into two files

Let's test this

Correction: It seems like i have to put everything into one file

```
❯ hashcat alphanumeric -a 0 -r chall3hash2lower.rule -r chall3hash2caeser.rule -r chall3hash2qwertyfixed.rule -r chall3hash2qwertyfixed2.rule --stdout
snvfrghjokl;,mp[wtdyibecux-123456789
bcdefghijkl,mopqrstuvwxyza0123456789
cdefghijkl,mopqrstuvwxyzab0123456789
defghijkl,mopqrstuvwxyzabc0123456789
efghijkl,mopqrstuvwxyzabcd0123456789
fghijkl,mopqrstuvwxyzabcde0123456789
ghijkl,mopqrstuvwxyzabcdef0123456789
hijkl,mopqrstuvwxyzabcdefg0123456789
ijkl,mopqrstuvwxyzabcdefgh0123456789
jkl,mopqrstuvwxyzabcdefghi0123456789
kl,mopqrstuvwxyzabcdefghij0123456789
l,mopqrstuvwxyzabcdefghijk0123456789
,mopqrstuvwxyzabcdefghijkl0123456789
mopqrstuvwxyzabcdefghijkl,0123456789
opqrstuvwxyzabcdefghijkl,m0123456789
pqrstuvwxyzabcdefghijkl,mo0123456789
qrstuvwxyzabcdefghijkl,mop0123456789
rstuvwxyzabcdefghijkl,mopq0123456789
stuvwxyzabcdefghijkl,mopqr0123456789
tuvwxyzabcdefghijkl,mopqrs0123456789
uvwxyzabcdefghijkl,mopqrst0123456789
vwxyzabcdefghijkl,mopqrstu0123456789
wxyzabcdefghijkl,mopqrstuv0123456789
xyzabcdefghijkl,mopqrstuvw0123456789
yzabcdefghijkl,mopqrstuvwx0123456789
zabcdefghijkl,mopqrstuvwxy0123456789
```

So let's do it in python and not use hashcat, as we will always get over the `31` rule limit (uppercase(1) + reverse(1) + digit to ngb(10) + 26). TLDR: This did not work and was buggy. I had a new idea:


## Pregenerate wordlist to reduce number of applied rules

```python
QWERTY = r"""
1 2 3 4 5 6 7 8 9 0 -
Q W E R T Y U I O P [
A S D F G H J K L ;
Z X C V B N M ,
""".replace(" ","").replace("\n","").lower()

from string import ascii_lowercase as LC, ascii_uppercase as UC
with open("chall3hash2.john","w") as f:
    for shift in range(26):
        # first, we upercase to prepare ceaser
        print("u",end="",file=f)
        # ceaser and qwerty sub
        for char in range(26):
            base_char   = UC[char]
            sub_char    = LC[(char + shift)%26]
            qwerty_char = QWERTY[QWERTY.index(sub_char) + 1]
            print(f"s{base_char}{qwerty_char}",end="",file=f)
        # print("s0-s90s89s78s67s56s45s34s23s12r",file=f)
```

- Via [--format](https://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats), we can supply the hash. (Does not work)

/Users/bluk/Developer/john/run/john --wordlist=rockyou.txt --rules chall3hash2.john --format=raw-sha256 <(echo "cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25e6af2b555f6f5")

- This is way to slow, so I just try to generate it in hashcat, do two passes and see

```
-rw-r--r--  1 bluk  staff   3.4G Jul 17 20:11 rockyou.chall3hash2.lst
-rw-r--r--  1 bluk  staff   133M Jul 15 14:52 rockyou.txt
```

## Apply the last rule and Reverse `r`

`s0-s90s89s78s67s56s45s34s23s12r` is the last part which we just do via hashcat. Honestly, could have just also put it into the code...

## Solution

```bash
❯ hashcat -O -a 0 -r chall3hash2final.rule -m 1400 cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25e6af2b555f6f5 rockyou.chall3hash2.lst
cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25e6af2b555f6f5:o4d@lkny@d
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1400 (SHA2-256)
Hash.Target......: cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25...55f6f5
Time.Started.....: Thu Jul 17 20:13:21 2025 (9 secs)
Time.Estimated...: Thu Jul 17 20:13:30 2025 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Base.......: File (rockyou.chall3hash2.lst)
Guess.Mod........: Rules (chall3hash2final.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 30013.8 kH/s (10.71ms) @ Accel:4096 Loops:1 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 256951170/372954010 (68.90%)
Rejected.........: 50050/256951170 (0.02%)
Restore.Point....: 255115954/372954010 (68.40%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 92hlmlvf -> 09jg;y[hj
Hardware.Mon.SMC.: Fan0: 0%, Fan1: 0%
Hardware.Mon.#1..: Util: 61%

Started: Thu Jul 17 20:13:03 2025
Stopped: Thu Jul 17 20:13:31 2025
```

## Steps:

1. ` python3 chall3gen2.py` to generate `chall3hash2.john`
    - Use uppercase
    - Apply 26 different ceaser's
    - Remap target ceaser to qwerty char
2. Generate candidates via `hashcat rockyou.txt -r chall3hash2.john --stdout > rockyou.chall3hash2.lst`
3. Use `echo "s0-s90s89s78s67s56s45s34s23s12r" > chall3hash2final.rule` to apply the final rule wich would be to much otherwise
4. Run `hashcat -O -a 0 -r chall3hash2final.rule -m 1400 cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25e6af2b555f6f5 rockyou.chall3hash2.lst`


# Password 3: Split the password in half, toggle the case of every consonant in the first half, randomly toggle the case of all vowels in the second half, then interleave the halves together. Assume password has an even length and is no more than 14 characters. The letter Y is considered a vowel for the purposes of this challenge.

> 84b9e0298b1beb5236b7fcd2dd67e67abf62d16fe6d591024178790238cb4453

- Split in password in half 
- Toggle consonants in the first half -> EVEN
- Randomly toggle vowels in the second half, vowels are `AEIOUY` -> $2 \cdot 2^6 = 128$ combinations via `s` -> ODD
- then interleave the halves together -> SWAP via `*MN`
- Passwords have even length and have less then 14 characters

abba12 -> aBBa12 -> aBBa12,aBBA12 -> aaB1B2,aAB1B2 


=> Due to the last requirement, we can do this with john as the password space reduces big

```bash
❯ awk '{ if (length % 2 == 0 && length <= 14) print $0 }' rockyou.txt > rockyou_filtered.txt
❯ wc -l rockyou*
  7749629 rockyou_filtered.txt
    59186 rockyou-75.txt
 14344392 rockyou.txt
```
- 

## Preprocessing: Transform everything that is a direct transformation 

We can split, toogle the first half and interleave without creating any new candidates

```python
import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    n = len(line)
    if (n&1 == 1) or (n > 14): continue
    n = n//2

    a, b = line[:n], line[n:]
    a = [(x.swapcase() if x.upper() in "AEIOUY" else x) for x in a]
    
    print("".join(a+b for a,b in zip(a,b)))
```

```bash
 echo "password" | python chall3gen3.py
PwaoSrSd
❯ cat rockyou.txt| python3 chall3gen3.py > rockyou_prefiltered
❯ wc -l rockyou*
 7749629 rockyou_filtered.txt
 7752322 rockyou_prefiltered
   59186 rockyou-75.txt
 14344392 rockyou.txt
 29905529 total
```

## Postprocessing the toggle for VOWELS

I believe it's faster if we just press it over hashcat. We can toogle with `T`. We only need to toggle at ODD indices, even when it is not a consonant.

We can toggle at `1,3,5,7,9,11,13` => `13579BE` as index for the toggle (hashcat uses letters for indicies bigger 9)

```python
print(":")
mask_size = 7
for toggle_states in range(1,1 << mask_size):
    for pos in range(mask_size):
        if toggle_states&1:
            index = "13579BE"[pos]
            print(f"T{index}",end="")
        toggle_states = toggle_states >> 1
    print("")
```

```bash
❯ hashcat -O -a 0 -r chall3hash3toggle.rule -m 1400 84b9e0298b1beb5236b7fcd2dd67e67abf62d16fe6d591024178790238cb4453 rockyou_filtered
84b9e0298b1beb5236b7fcd2dd67e67abf62d16fe6d591024178790238cb4453:CcoATnTdoyNY
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1400 (SHA2-256)
Hash.Target......: 84b9e0298b1beb5236b7fcd2dd67e67abf62d16fe6d59102417...cb4453
Time.Started.....: Thu Jul 17 22:20:24 2025 (0 secs)
Time.Estimated...: Thu Jul 17 22:20:24 2025 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Base.......: File (rockyou_filtered)
Guess.Mod........: Rules (chall3hash3toggle.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   500.2 MH/s (11.41ms) @ Accel:512 Loops:32 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 132120704/992297216 (13.31%)
Rejected.........: 128/132120704 (0.00%)
Restore.Point....: 917505/7752322 (11.84%)
Restore.Sub.#1...: Salt:0 Amplifier:32-64 Iteration:0-32
Candidate.Engine.: Device Generator
Candidates.#1....: LoorSr oPs -> BLLUoSoTD7
Hardware.Mon.SMC.: Fan0: 0%, Fan1: 0%
Hardware.Mon.#1..: Util: 87%

Started: Thu Jul 17 22:20:23 2025
Stopped: Thu Jul 17 22:20:24 2025
```

L3AK{er!bLigbroth1984_o4d@lkny@d_CcoATnTdoyNY}


# Gotchas

- Hashcat rules are super super super fast, better than generating stuff in python
- If it is getting to complex, pregenerate password with python (favour single transformations)
- For a `1 -> n` transformation, generate $n$ rules in hashcat as it is super fast
- Use `-O` to speed things up
- Make a break it you dont get further and use Chatty to proof your solutions. Usually, I had an easy solution at the end which did the job fine
- Read the documentation!!! Sadly, the $31$ limit was not that well explained when rules spread about many files :( Maybe it is a bug, I don't know ....
- Care for sequential processing in substitutions
- Write python scripts with `stdin` and `print` for bash power