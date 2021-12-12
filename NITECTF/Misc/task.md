> Description: We have captured Mr Brute who is a world renowned architect who has built the safest vault in the world which cannot be broken in anyway unless you have the password. He is also one of the biggest bee movie fans ever (His password was probably a word used in the movie). We were able to get the SHA-256 hash of the password from Mr.Brute by using extreme torture methods (Making him watch the bee movie 2398 times). During this torture, he told us that he was told to prepend the password with a salt before hashing it, so he uses 'salt' as a salt cuz salt is salt. He died soon after we released him (Got stung by a bee, obviously). BUT you have the hash. Decrypt the hash so you can break into his vault. hash = 12f3b9faec781b0e84184a6fa7c44c81416e5b1855633a2a2730295324724efe [Wrap the answer in flag format] Example :- nite{password} NOT nite{salt+password}


- target hash `12f3b9faec781b0e84184a6fa7c44c81416e5b1855633a2a2730295324724efe`
- salt `salt`
- Worlist: <https://gist.githubusercontent.com/The5heepDev/a15539b297a7862af4f12ce07fee6bb7/raw/7164813a9b8d0a3b2dcffd5b80005f1967887475/entire_bee_movie_script>

## Using hashcat

```
1420 | sha256($salt.$pass)                              | Raw Hash, Salted and/or Iterated
```

```
hashcat -m 1420 12f3b9faec781b0e84184a6fa7c44c81416e5b1855633a2a2730295324724efe:salt -a0 wordlist

12f3b9faec781b0e84184a6fa7c44c81416e5b1855633a2a2730295324724efe:salt:Oinnabon
```