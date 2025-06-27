#%%
output="""131
133
203
41
107
11
53
11
25
236
124
4
220
107
146
127
121
204
156
100
59
75
242
95
217
44
44
71
135
171
85
171
57
12
92
167
231
139
181
139
153
108
252
132
92
235
18
255
249
76
28
228
188
203
117
207
89
172
188
199
7
43
213
43
185
140
204
39
103
11
53
15
25
236
124
4
219
107
149
107
121
219
140
100
59
75
242
95
217
44
44
68
155
171
85
175
57
27
76
164
252
139
181
143
153
108
252
135
71
235
21
239
249
76
28
228
187
203
117
207
89
187
172
196
27
43
213
43
185
140
204
36
124
11
53
15
25
236
105
115
141
91
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
