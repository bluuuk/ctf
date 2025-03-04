

We have 

```c
{
    if (arg1 == 3)
        return puts("-- ERROR -- [That memory has bee…");
    
    if ((arg1 > 3 || arg1 < 0))
        return puts("-- ERROR -- [That memory does no…");
    
    void* rax_3 = &messages[((int64_t)arg1)];
    int64_t var_28 = -0x3c1d50e171252b3a;
    int64_t var_20_1 = -0x119fdab73f2bf9f4;
    int32_t var_c_1 = 0;
    
    while (*(uint8_t*)((char*)rax_3 + ((int64_t)var_c_1)) != 0)
    {
        int32_t temp0_1;
        int32_t temp1_1;
        temp0_1 = HIGHD(((int64_t)var_c_1));
        temp1_1 = LOWD(((int64_t)var_c_1));
        uint32_t rdx_4 = (temp0_1 >> 0x1c);
        putchar(((int32_t)(*(uint8_t*)(&var_28 + ((int64_t)(((temp1_1 + rdx_4) & 0xf) - rdx_4))) ^ *(uint8_t*)((char*)rax_3 + ((int64_t)var_c_1)))));
        var_c_1 += 1;
    }
    
    return puts(&data_21d5);
}
```

However, looking at `void* rax_3 = &messages[((int64_t)arg1)];`, espacially `messages`, we have 

```c
char* messages[0x4] = 
{
    [0x0] = 0x2008
    [0x1] = 0x2068
    [0x2] = 0x20f0
    [0x3] = 0x2128
}
```

The check at the start 
```c
    if (arg1 == 3)
        return puts("-- ERROR -- [That memory has bee…");
```

forbids us, but we would like to read the memory with arg1 == 3, therefore, we patch this to never use the branch :) Voila option 3 gives us the flag.