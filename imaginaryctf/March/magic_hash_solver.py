#%%
import subprocess
import tempfile
from assets import pymd5 
from base64 import b64decode,b64encode
from hashlib import md5, sha3_256
from zlib import crc32
import random
from itertools import product
import numpy as np 

def magic_hash(x):
    h = md5(x).digest()
    h += crc32(h + x).to_bytes(4, "little")
    return sha3_256(h).digest()

# Create two temporary files
def generate_collision(previous_hash : bytearray):
    with tempfile.NamedTemporaryFile() as temp_file1, tempfile.NamedTemporaryFile() as temp_file2:
        
        # Get the paths of the temporary files
        output_file1 = temp_file1.name
        output_file2 = temp_file2.name

        # Construct the command as a list of arguments
        command = [
            "/Users/bluk/Developer/md5collgen/md5collgen",
            '-i', previous_hash.hex(),
            '-o', output_file1,output_file2, '-q'
        ]

        # Execute the command
        subprocess.run(command,capture_output=False,stdout = subprocess.DEVNULL)
        
        return list(map(lambda x:x.read(),[temp_file1,temp_file2]))

def generate_inital_collision():
    with tempfile.NamedTemporaryFile() as temp_input_file, tempfile.NamedTemporaryFile() as temp_file1, tempfile.NamedTemporaryFile() as temp_file2:
        
        # Get the paths of the temporary files
        output_file1 = temp_file1.name
        output_file2 = temp_file2.name
        input_file   = temp_input_file.name
        
        temp_input_file.write(random.randbytes(64))
        temp_input_file.flush()

        # Construct the command as a list of arguments
        command = [
            "/Users/bluk/Developer/md5collgen/md5collgen",
            input_file,
            '-o', output_file1,output_file2, '-q'
        ]

        # Execute the command
        subprocess.run(command,capture_output=False,stdout = subprocess.DEVNULL)
        
        return list(map(lambda x:x.read(),[temp_file1,temp_file2]))

#%%
a,b = generate_inital_collision()
len(a)
#%%
condition = True
while condition:
    a,b = generate_inital_collision()

    blocks1 = [a]
    blocks2 = [b]
    padding = []

    last = None
    count = 0
    input = blocks1[0]

    # for i in range(21):
    for i in range(27):
        print(i,": ",len(input))
        base = pymd5.md5(input)
        last = base.digest_nopad()
        #last = md5(input).digest()
        
        # if not all(last == md5(other).digest() for other in all_inputs):
        #     for val in all_inputs:
        #         print(md5(val).digest().hex())
        #     break
        
        a,b = generate_collision(last)
        # print("Collisions at: ",end="")
        # for i,(aa,bb) in enumerate(zip(a,b)):
        #     if aa != bb:print(f"{i}".rjust(2,"0"),end=", ")
        # print()
        
        assert len(a) == len(b)
        assert a != b
        
        # old_pad = pymd5.padding(len(input)*8)
        blocks1.append(a)
        blocks2.append(b)
        # padding.append(old_pad)
        
        input += a

    print(len(input),len(blocks1),len(blocks2))

    ground_input = input
    ground_hash = md5(ground_input).digest()
    # suffix_len = 4321 - len(ground_input) 
    # suffix = random.randbytes(suffix_len)
    # print(f"Trying {suffix_len=}")
    suffix = b""
    
    truth_input = ground_input + suffix
    truth_hash = md5(truth_input).digest()
    seen = np.zeros(2**32,dtype=np.uint32)
    input = b"" 

    for index in range(2**(len(blocks1))-1,-1,-1):
        testcase = []
        for i in range(len(blocks1)):
            if (index >> i) & 1:
                testcase.append(blocks1[i])
            else:
                testcase.append(blocks2[i])
                
        input = b"".join(testcase)
        
        # assert len(input) == len(truth_input)
        # assert index == 0 or input != truth_input
        # assert truth_hash == md5(input).digest()
        compare_hash = crc32(truth_hash + input) & 0xFFFFFFFF
        
        if seen[compare_hash] > 0:
            aindex = index 
            bindex = seen[compare_hash]
            
            assert aindex != bindex
            
            print(aindex,b64encode(input))
            
            testcase = []
            for i in range(len(blocks1)):
                if (index >> i) & 1:
                    testcase.append(blocks1[i])
                else:
                    testcase.append(blocks2[i])
                    
            otherinput = b"".join(testcase)
                
            print(bindex,b64encode(otherinput))
            condition = False
            assert magic_hash(input) == magic_hash(otherinput)
            break
            
        seen[compare_hash] = index

    print(index,len(seen))
# %%
