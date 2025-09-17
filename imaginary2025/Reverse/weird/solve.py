def reverse_transform(res: str) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = r"!@#$%^&*()_+{}[]|"
    
    flag = []
    
    for i, ch in enumerate(res):
        if ch in letters:
            c = (letters.index(ch) - i) % len(letters)
            flag.append(letters[c])
        elif ch in digits:
            c2 = (digits.index(ch) - 2*i) % len(digits)
            flag.append(digits[c2])
        elif ch in symbols:
            c3 = (symbols.index(ch) - i*i)
            # if c3 < 0:
            #     c3 = -(abs(c3) % len(symbols))
            c3 = c3 % len(symbols)
            flag.append(symbols[c3])
        else:
            # Preserve unknown characters
            print("Unknown",ch)
            flag.append(ch)
    
    return "".join(flag)

# Example usage
transformed = "idvi+1{s6e3()arg2zv[moqa905+"  # Example transformed string
original = reverse_transform(transformed)
print(original)

# this spits out "ictf{1_l0v3&@ndr0id_stud103}" but some thinking after tells me it should be 
# ictf{1_l0v3 -> _ <- @ndr0id_stud103}

# I really don't know where the error comes from