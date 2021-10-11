import subprocess
import time
import string
from pathlib import Path
import re

with open("cpp.c","r") as f:
    source_code = f.read()

timings = []
output = set()

for char in string.digits + string.ascii_letters:

    proc = subprocess.Popen(['gcc','-x','c','-'],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    
    source = re.sub(r"#define FLAG_4 CHAR_[\w\d]",f"#define FLAG_4 CHAR_{char}",source_code)

    #with (Path.cwd() / "test").open("w") as f:
    #    f.write(source)
    #break

    start = time.time()

    stdout_data = proc.communicate(
        input=bytes(source,"ASCII")
    )[1]
    #print(stdout_data)
    #break
    end = time.time()

    timings.append(end-start)
    output.add(stdout_data)

print(sorted(timings))
print(output)