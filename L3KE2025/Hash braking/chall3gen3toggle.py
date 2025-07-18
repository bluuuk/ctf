print(":")
mask_size = 7
for toggle_states in range(1,1 << mask_size):
    for pos in range(mask_size):
        if toggle_states&1:
            index = "13579BE"[pos]
            print(f"T{index}",end="")
        toggle_states = toggle_states >> 1
    print("")