import sys
vowels = set("AEIOUYaeiouy")

for line in sys.stdin:
    line = line.rstrip("\n")
    n = len(line)
    if (n&1 == 1) or (n > 14): continue
    n = n//2

    a, b = line[:n], line[n:]
    a = [(x if x in vowels else x.swapcase()) for x in a]
    
    print("".join(a+b for a,b in zip(a,b)))