password = "lp`7a<qLw\x1ekHopt(f-f*,o}V\x0f\x15J"
pw_bytes = bytearray(password,encoding="utf-8")

for i in range(len(pw_bytes)):
    pw_bytes[i] = pw_bytes[i] + 2
    pw_bytes[i] = pw_bytes[i] ^ (i+10)


print(pw_bytes)

"""
    while (index < (int)read_bytes + -1) {
        inputbuffer[index] = (inputbuffer[index] ^ ((char)index + 10U)) - 2;
        // https://en.cppreference.com/w/c/language/operator_precedence 
        // plus precedence > xor precedence
        index = index + 1;
    }
"""