#%%
output="""105
147
233
7
81
145
253
56
71
153
249
2
105
163
199
6
24
162
211
2
98
162
152
56
71
137
236
22
95
161
253
26
92
163
199
112
77
150
199
44
64
164
237
121
83
137
239
6
89
154
199
5
77
150
237
6
95
154
152
120
77
146
152
121
89
154
195
2
105
163
199
6
24
162
211
2
109
162
153
40
26
163
199
121
26
137
236
10
92
162
253
22
92
137
236
10
92
162
253
22
92
137
236
22
95
161
253
26
92
163
199
112
77
149
199
121
94
154
253
120
77
146
253
14
69
162
211
2
121
162
152
113
70
162
211
1
23
189
"""
output = list(map(int,output.splitlines()))
output

#%%
N = 0xFF + 1
63 * 191 % N

# 192 = a * 42 + b <=> 192-a*42 = b
# 170 = a * 192 + b <=> 

# 170 = a * 192 + 192 -a * 42 
# 170 - 192 = a * (192 - 42)

(170 - 192) * pow(192 - 42 + N,-1,N)

#%%
# output is just the numbers given

known = zip(output,map(ord,"CSCG{"))
known_output = [a^b for a,b in known]
known_output

# %%
import itertools

start = itertools.product(range(1,255),range(0,255))
for last,target in zip(known_output,known_output[1:]):
    start = [
        (a,b) for a,b in start if (a * last + b) % N == target
    ]

start

# %%
sol = set()

for a,b in start:
    last = output[0] ^ ord("C")
    chars = ["C"]
    for val in output[1:]: #SCG{
        last = (a * last + b) % N 
        chars.append(chr(last ^ val))
    sol.add("".join(chars))
        
sol
# %%
import base64
base64.b64decode("QWxmYSBCcmF2byBHb2xmIFVuaWZvcm0gVmljdG9yIEFsZmEgVGFuZ28gR29sZiBCcmF2byBGb3h0cm90IFJvbWVvIFJvbWVvIFVuaWZvcm0gUm9tZW8gRWNobyBSb21lbyA=")
# %%
