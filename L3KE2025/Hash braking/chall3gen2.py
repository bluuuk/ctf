from string import ascii_lowercase as LC, ascii_uppercase as UC

QWERTY = r"""
1 2 3 4 5 6 7 8 9 0 -
Q W E R T Y U I O P [
A S D F G H J K L ;
Z X C V B N M ,
""".replace(" ","").replace("\n","").lower()

with open("chall3hash2.john","w") as f:
    for shift in range(26):
        # first, we upercase to prepare ceaser
        print("u",end="",file=f)
        # ceaser and qwerty sub
        for char in range(26):
            base_char   = UC[char]
            sub_char    = LC[(char + shift)%26]
            qwerty_char = QWERTY[QWERTY.index(sub_char) + 1]
            print(f"s{base_char}{qwerty_char}",end="",file=f)
        print(file=f)
        #print("s0-s90s89s78s67s56s45s34s23s12r",file=f)