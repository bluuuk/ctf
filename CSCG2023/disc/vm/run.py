import os

def main():
    code = bytes.fromhex(input("Give me your code in hex:"))

    with open("/tmp/code", "wb") as fout:
        fout.write(code)

    os.execv("./vm", ["./vm", "/tmp/code"])


if __name__ == '__main__':
    main()
