import sys

"""
0) We have 16 outputs, thus the flag length is 16
1) Every two entries form a pair as the top of the heap is poped twice each iteration
2) We first deduct if the entry was passed thru even/odd
    - its even if it is a palindrome: val1 + val3 + ii + reverse(val1 + val3)
    - its odd otherwise: int(string(val1) + string(val3) + string(ii))
3) we try to reverse the index i
    - for even, its the middle of the palindrome
    - for odd, it should be the end with unique numbers from {0..15}
4) now we extract val1 and val3
    - for even, always check if the ascii range matches
    - for odd, always check if ascii range matches
5) combine them together again, with each a pair as they were intervened
    - place them back at the respective index

Ascii chars are inbetween 32 and 127
Filter with `rg -o -e '\((\d+),(\d+)\)[^>]+> (\d+)' -r '$1, $2, $3'`

and solve with

```bash
❯ rg -o -e '\((\d+),(\d+)\)[^>]+> (\d+)' -r '$1, $2, $3' output\(1\).txt | python3 combine.py
ictf{cu3st0m_c0mp@r@t0rs_1e8f9e}
```

by assembling everything together. Assmble:

Given two pairs, sequentially, we recombine them as they are interleaved with the min heap

```python3
    line = sys.stdin.readline()
    if not line: break
    
    a0,b0,c0 = list(map(int,line.strip().split(",")))

    line = sys.stdin.readline()
    a1,b1,c1 = list(map(int,line.strip().split(",")))
    
    a = chr(a0) + chr(a1)
    b = chr(b0) + chr(b1)

    d[c0] = a
    d[c1] = b
```
"""

d = [None]*16

while not sys.stdin.closed:
    line = sys.stdin.readline()
    if not line: break
    
    a0,b0,c0 = list(map(int,line.strip().split(",")))

    line = sys.stdin.readline()
    a1,b1,c1 = list(map(int,line.strip().split(",")))
    
    a = chr(a0) + chr(a1)
    b = chr(b0) + chr(b1)

    d[c0] = a
    d[c1] = b

print("".join(d))
    