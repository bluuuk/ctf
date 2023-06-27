#!/usr/bin/python3


from posixpath import split
from sys import flags
from traceback import print_stack


sample_flag = "CSCG{" + "x" * (41 - 1 - 5) + "}"

assert len(sample_flag) == 41
"""
We need to solve

ord(flag[-1]) - (len(flag) * 3 + 5 - 3) == 0

We know that the flag has the format of "CSCG{xxx}" such that we can fill in values and rearange:

(len(flag) * 3 + 5 - 3) == ord(flag[-1])

(len(flag) * 3 + 5 - 3) == ord("}")

(len(flag) * 3 + 5 - 3) == 125

len(flag) = 123/3 = 41

so we can continue with CSCG{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
"""

print(sample_flag)

array = "Decompile This Small Application, Analyze It And Get The Flag!".split(
    " ")

rmrf = [
    0,
    4,
    6,
    7,
    8,
    9
]

flag = "CSCG{" + "_".join([array[x] for x in rmrf]) + "}"

assert len(flag) == 41

print(flag)
"""
inner_flag = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

for i in rmrf:
    current_word = array[i]

    matches = len(list(filter(
        lambda x: x, [inner_flag[j] == current_word[j]
                      for j in range(len(current_word))]
    )))

    if matches == len(current_word) and 

    print(matches)
"""
