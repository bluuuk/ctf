

"""
❯ file chal
chal: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=b133fed426c2cab7896924398dc13b366a8dbd38, for GNU/Linux 3.2.0, not stripped

❯ checksec chal
[*] '/home/kali/Developer/ctf/googlebeginner2025/simple_echo/chal'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    Stripped:   No


%% https://stackoverflow.com/questions/79422665/partial-vs-full-relro
❯ readelf --program-headers --wide chal

Elf file type is DYN (Position-Independent Executable file)
Entry point 0x1080
There are 13 program headers, starting at offset 64

Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  PHDR           0x000040 0x0000000000000040 0x0000000000000040 0x0002d8 0x0002d8 R   0x8
  INTERP         0x000318 0x0000000000000318 0x0000000000000318 0x00001c 0x00001c R   0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x000000 0x0000000000000000 0x0000000000000000 0x000720 0x000720 R   0x1000
  LOAD           0x001000 0x0000000000001000 0x0000000000001000 0x0001e9 0x0001e9 R E 0x1000
  LOAD           0x002000 0x0000000000002000 0x0000000000002000 0x00010c 0x00010c R   0x1000
  LOAD           0x002dd0 0x0000000000003dd0 0x0000000000003dd0 0x000260 0x000270 RW  0x1000
  DYNAMIC        0x002de0 0x0000000000003de0 0x0000000000003de0 0x0001e0 0x0001e0 RW  0x8
  NOTE           0x000338 0x0000000000000338 0x0000000000000338 0x000020 0x000020 R   0x8
  NOTE           0x000358 0x0000000000000358 0x0000000000000358 0x000044 0x000044 R   0x4
  GNU_PROPERTY   0x000338 0x0000000000000338 0x0000000000000338 0x000020 0x000020 R   0x8
  GNU_EH_FRAME   0x002034 0x0000000000002034 0x0000000000002034 0x00002c 0x00002c R   0x4
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0x10
  GNU_RELRO      0x002dd0 0x0000000000003dd0 0x0000000000003dd0 0x000230 0x000230 R   0x1

 Section to Segment mapping:
  Segment Sections...
   00     
   01     .interp 
   02     .interp .note.gnu.property .note.gnu.build-id .note.ABI-tag .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt 
   03     .init .plt .plt.got .text .fini 
   04     .rodata .eh_frame_hdr .eh_frame 
   05     .init_array .fini_array .dynamic .got .got.plt .data .bss 
   06     .dynamic 
   07     .note.gnu.property 
   08     .note.gnu.build-id .note.ABI-tag 
   09     .note.gnu.property 
   10     .eh_frame_hdr 
   11     
   12     .init_array .fini_array .dynamic .got 


.got --> global variables
.got.plt --> global function


----

int32_t main(int32_t argc, char** argv, char** envp)
    int32_t argc_1 = argc
    char** argv_1 = argv
    printf(format: "Type input to be echoed: ")
    fflush(fp: __TMC_END__)
    char format[0x40] #63 + NB
    __isoc99_scanf(format: "%63s", &format) # %[*][width][length]specifier -> s: 
    puts(str: "Echoed output: ")
    printf(format: &format)
    return 0


scanf:
    s -> Any number of non-whitespace characters, stopping at the first whitespace character found. A terminating null character is automatically added at the end of the stored sequence.
    63 -> read 63 bytes and add a NULL



"""