```
❯ hashcat --help | grep -i SHA2-256
   1400 | SHA2-256                                                   | Raw Hash
```

hash cat rules based attacks:

- mode `a 0`
- `-r` for a rule file

# Refresher on attack modes

| Name | Mode | Description |
| - | - | - | 
| Dictionary attack | 0 | trying all words in a list; also called “straight” mode |
| Combinator attack | 1 | concatenating words from multiple wordlists  |
| Brute-force attack and Mask attack | 3 | trying all characters from given charsets, per position |
| Hybrid attack | 6/7 | combining wordlists+masks (-a 6) and masks+wordlists (-a 7); can also be done with rules |
| Association attack | 9 | use an username, a filename, a hint, or any other pieces of information which could have had an influence in the password generation to attack one specific hash |
| Rule-based attack | 0,6,7 | applying rules to words from wordlists; combines with wordlist-based attacks |
| Toggle-case attack | X | toggling case of characters; now accomplished with rules |

```bash
  Attack-          | Hash- |
  Mode             | Type  | Example command
 ==================+=======+==================================================================
  Wordlist         | $P$   | hashcat -a 0 -m 400 example400.hash example.dict
  Wordlist + Rules | MD5   | hashcat -a 0 -m 0 example0.hash example.dict -r rules/best64.rule
  Brute-Force      | MD5   | hashcat -a 3 -m 0 example0.hash ?a?a?a?a?a?a
  Combinator       | MD5   | hashcat -a 1 -m 0 example0.hash example.dict example.dict
  Association      | $1$   | hashcat -a 9 -m 500 example500.hash 1word.dict -r rules/best64.rule
```

# Password 1: Append 3 characters at the end, in the following order: a special character, a number, and an uppercase letter

Looks like a hybrid attack aka wordlist+mask $\implies a=6$

```bash
    ?l = abcdefghijklmnopqrstuvwxyz
    ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ?d = 0123456789
    ?h = 0123456789abcdef
    ?H = 0123456789ABCDEF
    ?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    ?a = ?l?u?d?s
    ?b = 0x00 - 0xff
```

mask = ?s?d?u


```bash
hashcat -m 1400 5e09f66ae5c6b2f4038eba26dc8e22d8aeb54f624d1d3ed96551e900dac7cf0d -a 6 rockyou.txt "?s?d?u"
```

It is `-m MODE HASH -a ATTACK PARAM1 PARAM2 ...`

> 5e09f66ae5c6b2f4038eba26dc8e22d8aeb54f624d1d3ed96551e900dac7cf0d:hyepsi^4B

However, checking the benchmark, we are quite slow with `420.8 MH/s`

```
---------------------------
* Hash-Mode 1400 (SHA2-256)
---------------------------

Speed.#1.........:   862.6 MH/s (67.11ms) @ Accel:256 Loops:256 Thr:64 Vec:1
```

# Password 2: A typo was made when typing the password. Consider a typo to mean a single-character deletion from the password

1. `Rockyou` is full of trash, so I got myself a smaller version from `https://github.com/danielmiessler/SecLists`
2. We have to figure out the maximum length to delete a random char 

```bash
❯ cat rockyou-75.txt | awk ' { if ( length > x ) { x = length; y = $0 } }END{ print y }'
Lets you update your FunNotes and more!
❯ cat rockyou-75.txt | awk ' { if ( length > x ) { x = length; y = $0 } }END{ print x }'
39
```

3. The rule to delete a char is `D<Position>` 
4. So just write a python script `python3 -c "[print(f'D{x}') for x in range(40)]" > chall2hash2.rule`

However, I have to read better `Indicates that N starts at 0. For character positions other than 0-9 use A-Z (A=10)`

5. So just write a python script `python3 -c "import string;[print(f'D{x}') for x in string.digits + string.ascii_uppercase]" > chall2hash2.rule`

It's enough for 36 chars so lets go.


```bash
❯ hashcat -a 0 -r chall2hash2.rule -m 1400 fb58c041b0059e8424ff1f8d2771fca9ab0f5dcdd10c48e7a67a9467aa8ebfa8 rockyou.txt
fb58c041b0059e8424ff1f8d2771fca9ab0f5dcdd10c48e7a67a9467aa8ebfa8:thecowsaysmo
```

However, rockyou-75 sucks here:

```bash
❯ grep "thecowsays" rockyou.txt
thecowsaysmoo
thecowsaysmoo2007
❯ grep "thecowsays" rockyou-75.txt
```

# Password 3: Make the password leet (and since I'm nice, I'll tell you a hint: only vowels are leetified!)

- This is just a basic substitution with `sXY` with X -> Y

If we choose `sA4sa4sE3se3sI1si1so0sO0` as a single rule, we do not run into any wins

```bash
❯ hashcat -a 0 -r chall2hash2.rule -m 1400 4ac53d04443e6786752ac78e2dc86f60a629e4639edacc6a5937146f3eacc30f rockyou.txt
4ac53d04443e6786752ac78e2dc86f60a629e4639edacc6a593...acc30f
```

It is actually okay just to do a single char to char replacement if we take the table from [wikipedia](https://en.wikipedia.org/wiki/Leet)

```
a → 4, /\, @, /-\, ^, (L, Д
e → 3, &, £, €, [-, |=-
i → 1, |, ][, !, eye, 3y3
o → 0, (), oh, [], p, <>, Ø
u → (_), |_|, v, L|, บ
```

So we split in into multiple files and apply all :)

```bash
❯ hashcat -a 0 -r chall2hash3a.rule -r chall2hash3e.rule -r chall2hash3i.rule -r chall2hash3u.rule -r chall2hash3o.rule -m 1400 4ac53d04443e6786752ac78e2dc86f60a629e4639edacc6a5937146f3eacc30f rockyou.txt
4ac53d04443e6786752ac78e2dc86f60a629e4639edacc6a5937146f3eacc30f:unf0rg1v@bl3
```

5e09f66ae5c6b2f4038eba26dc8e22d8aeb54f624d1d3ed96551e900dac7cf0d:hyepsi^4B
fb58c041b0059e8424ff1f8d2771fca9ab0f5dcdd10c48e7a67a9467aa8ebfa8:thecowsaysmo
4ac53d04443e6786752ac78e2dc86f60a629e4639edacc6a5937146f3eacc30f:unf0rg1v@bl3

L3AK{hyepsi^4B_thecowsaysmo_unf0rg1v@bl3}