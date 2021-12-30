
readflag:     Dateiformat elf64-x86-64


Disassembly of section .init:

0000000000001000 <.init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    rsp,0x8
    1008:	48 8b 05 b9 2f 00 00 	mov    rax,QWORD PTR [rip+0x2fb9]        # 0x3fc8
    100f:	48 85 c0             	test   rax,rax
    1012:	74 02                	je     0x1016
    1014:	ff d0                	call   rax
    1016:	48 83 c4 08          	add    rsp,0x8
    101a:	c3                   	ret    

Disassembly of section .text:

0000000000001020 <.text>:
    1020:	55                   	push   rbp
    1021:	66 0f ef c0          	pxor   xmm0,xmm0
    1025:	b9 3e 00 00 00       	mov    ecx,0x3e
    102a:	53                   	push   rbx
    102b:	48 81 ec 18 02 00 00 	sub    rsp,0x218
    1032:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
    1039:	00 00 
    103b:	48 89 84 24 08 02 00 	mov    QWORD PTR [rsp+0x208],rax
    1042:	00 
    1043:	31 c0                	xor    eax,eax
    1045:	48 8d 7c 24 10       	lea    rdi,[rsp+0x10]
    104a:	0f 29 04 24          	movaps XMMWORD PTR [rsp],xmm0
    104e:	f3 48 ab             	rep stos QWORD PTR es:[rdi],rax
    1051:	ff 15 81 2f 00 00    	call   QWORD PTR [rip+0x2f81]        # 0x3fd8
    1057:	89 c3                	mov    ebx,eax
    1059:	ff 15 71 2f 00 00    	call   QWORD PTR [rip+0x2f71]        # 0x3fd0
    105f:	39 c3                	cmp    ebx,eax
    1061:	74 71                	je     0x10d4
    1063:	be 00 00 08 00       	mov    esi,0x80000
    1068:	48 8d 3d 4a 10 00 00 	lea    rdi,[rip+0x104a]        # 0x20b9
    106f:	31 c0                	xor    eax,eax
    1071:	ff 15 69 2f 00 00    	call   QWORD PTR [rip+0x2f69]        # 0x3fe0
    1077:	89 c5                	mov    ebp,eax
    1079:	85 c0                	test   eax,eax
    107b:	78 7e                	js     0x10fb
    107d:	48 89 e3             	mov    rbx,rsp
    1080:	eb 19                	jmp    0x109b
    1082:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    1088:	48 89 de             	mov    rsi,rbx
    108b:	bf 01 00 00 00       	mov    edi,0x1
    1090:	ff 15 12 2f 00 00    	call   QWORD PTR [rip+0x2f12]        # 0x3fa8
    1096:	48 85 c0             	test   rax,rax
    1099:	78 48                	js     0x10e3
    109b:	ba 00 02 00 00       	mov    edx,0x200
    10a0:	48 89 de             	mov    rsi,rbx
    10a3:	89 ef                	mov    edi,ebp
    10a5:	ff 15 0d 2f 00 00    	call   QWORD PTR [rip+0x2f0d]        # 0x3fb8
    10ab:	48 89 c2             	mov    rdx,rax
    10ae:	48 85 c0             	test   rax,rax
    10b1:	7f d5                	jg     0x1088
    10b3:	75 64                	jne    0x1119
    10b5:	48 8b 84 24 08 02 00 	mov    rax,QWORD PTR [rsp+0x208]
    10bc:	00 
    10bd:	64 48 2b 04 25 28 00 	sub    rax,QWORD PTR fs:0x28
    10c4:	00 00 
    10c6:	75 4b                	jne    0x1113
    10c8:	48 81 c4 18 02 00 00 	add    rsp,0x218
    10cf:	31 c0                	xor    eax,eax
    10d1:	5b                   	pop    rbx
    10d2:	5d                   	pop    rbp
    10d3:	c3                   	ret    
    10d4:	48 8d 3d 2d 0f 00 00 	lea    rdi,[rip+0xf2d]        # 0x2008
    10db:	ff 15 bf 2e 00 00    	call   QWORD PTR [rip+0x2ebf]        # 0x3fa0
    10e1:	eb 80                	jmp    0x1063
    10e3:	48 8d 3d 86 0f 00 00 	lea    rdi,[rip+0xf86]        # 0x2070
    10ea:	ff 15 b0 2e 00 00    	call   QWORD PTR [rip+0x2eb0]        # 0x3fa0
    10f0:	bf 01 00 00 00       	mov    edi,0x1
    10f5:	ff 15 ed 2e 00 00    	call   QWORD PTR [rip+0x2eed]        # 0x3fe8
    10fb:	48 8d 3d 3e 0f 00 00 	lea    rdi,[rip+0xf3e]        # 0x2040
    1102:	ff 15 98 2e 00 00    	call   QWORD PTR [rip+0x2e98]        # 0x3fa0
    1108:	bf 01 00 00 00       	mov    edi,0x1
    110d:	ff 15 d5 2e 00 00    	call   QWORD PTR [rip+0x2ed5]        # 0x3fe8
    1113:	ff 15 97 2e 00 00    	call   QWORD PTR [rip+0x2e97]        # 0x3fb0
    1119:	48 8d 3d 78 0f 00 00 	lea    rdi,[rip+0xf78]        # 0x2098
    1120:	ff 15 7a 2e 00 00    	call   QWORD PTR [rip+0x2e7a]        # 0x3fa0
    1126:	bf 01 00 00 00       	mov    edi,0x1
    112b:	ff 15 b7 2e 00 00    	call   QWORD PTR [rip+0x2eb7]        # 0x3fe8
    1131:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
    1138:	00 00 00 
    113b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    1140:	f3 0f 1e fa          	endbr64 
    1144:	31 ed                	xor    ebp,ebp
    1146:	49 89 d1             	mov    r9,rdx
    1149:	5e                   	pop    rsi
    114a:	48 89 e2             	mov    rdx,rsp
    114d:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
    1151:	50                   	push   rax
    1152:	54                   	push   rsp
    1153:	4c 8d 05 56 01 00 00 	lea    r8,[rip+0x156]        # 0x12b0
    115a:	48 8d 0d df 00 00 00 	lea    rcx,[rip+0xdf]        # 0x1240
    1161:	48 8d 3d b8 fe ff ff 	lea    rdi,[rip+0xfffffffffffffeb8]        # 0x1020
    1168:	ff 15 52 2e 00 00    	call   QWORD PTR [rip+0x2e52]        # 0x3fc0
    116e:	f4                   	hlt    
    116f:	90                   	nop
    1170:	48 8d 3d 99 2e 00 00 	lea    rdi,[rip+0x2e99]        # 0x4010
    1177:	48 8d 05 92 2e 00 00 	lea    rax,[rip+0x2e92]        # 0x4010
    117e:	48 39 f8             	cmp    rax,rdi
    1181:	74 15                	je     0x1198
    1183:	48 8b 05 0e 2e 00 00 	mov    rax,QWORD PTR [rip+0x2e0e]        # 0x3f98
    118a:	48 85 c0             	test   rax,rax
    118d:	74 09                	je     0x1198
    118f:	ff e0                	jmp    rax
    1191:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1198:	c3                   	ret    
    1199:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    11a0:	48 8d 3d 69 2e 00 00 	lea    rdi,[rip+0x2e69]        # 0x4010
    11a7:	48 8d 35 62 2e 00 00 	lea    rsi,[rip+0x2e62]        # 0x4010
    11ae:	48 29 fe             	sub    rsi,rdi
    11b1:	48 89 f0             	mov    rax,rsi
    11b4:	48 c1 ee 3f          	shr    rsi,0x3f
    11b8:	48 c1 f8 03          	sar    rax,0x3
    11bc:	48 01 c6             	add    rsi,rax
    11bf:	48 d1 fe             	sar    rsi,1
    11c2:	74 14                	je     0x11d8
    11c4:	48 8b 05 25 2e 00 00 	mov    rax,QWORD PTR [rip+0x2e25]        # 0x3ff0
    11cb:	48 85 c0             	test   rax,rax
    11ce:	74 08                	je     0x11d8
    11d0:	ff e0                	jmp    rax
    11d2:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    11d8:	c3                   	ret    
    11d9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    11e0:	f3 0f 1e fa          	endbr64 
    11e4:	80 3d 25 2e 00 00 00 	cmp    BYTE PTR [rip+0x2e25],0x0        # 0x4010
    11eb:	75 33                	jne    0x1220
    11ed:	55                   	push   rbp
    11ee:	48 83 3d 02 2e 00 00 	cmp    QWORD PTR [rip+0x2e02],0x0        # 0x3ff8
    11f5:	00 
    11f6:	48 89 e5             	mov    rbp,rsp
    11f9:	74 0d                	je     0x1208
    11fb:	48 8b 3d 06 2e 00 00 	mov    rdi,QWORD PTR [rip+0x2e06]        # 0x4008
    1202:	ff 15 f0 2d 00 00    	call   QWORD PTR [rip+0x2df0]        # 0x3ff8
    1208:	e8 63 ff ff ff       	call   0x1170
    120d:	c6 05 fc 2d 00 00 01 	mov    BYTE PTR [rip+0x2dfc],0x1        # 0x4010
    1214:	5d                   	pop    rbp
    1215:	c3                   	ret    
    1216:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
    121d:	00 00 00 
    1220:	c3                   	ret    
    1221:	66 66 2e 0f 1f 84 00 	data16 nop WORD PTR cs:[rax+rax*1+0x0]
    1228:	00 00 00 00 
    122c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    1230:	f3 0f 1e fa          	endbr64 
    1234:	e9 67 ff ff ff       	jmp    0x11a0
    1239:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1240:	f3 0f 1e fa          	endbr64 
    1244:	41 57                	push   r15
    1246:	4c 8d 3d 73 2b 00 00 	lea    r15,[rip+0x2b73]        # 0x3dc0
    124d:	41 56                	push   r14
    124f:	49 89 d6             	mov    r14,rdx
    1252:	41 55                	push   r13
    1254:	49 89 f5             	mov    r13,rsi
    1257:	41 54                	push   r12
    1259:	41 89 fc             	mov    r12d,edi
    125c:	55                   	push   rbp
    125d:	48 8d 2d 64 2b 00 00 	lea    rbp,[rip+0x2b64]        # 0x3dc8
    1264:	53                   	push   rbx
    1265:	4c 29 fd             	sub    rbp,r15
    1268:	48 83 ec 08          	sub    rsp,0x8
    126c:	e8 8f fd ff ff       	call   0x1000
    1271:	48 c1 fd 03          	sar    rbp,0x3
    1275:	74 1f                	je     0x1296
    1277:	31 db                	xor    ebx,ebx
    1279:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1280:	4c 89 f2             	mov    rdx,r14
    1283:	4c 89 ee             	mov    rsi,r13
    1286:	44 89 e7             	mov    edi,r12d
    1289:	41 ff 14 df          	call   QWORD PTR [r15+rbx*8]
    128d:	48 83 c3 01          	add    rbx,0x1
    1291:	48 39 dd             	cmp    rbp,rbx
    1294:	75 ea                	jne    0x1280
    1296:	48 83 c4 08          	add    rsp,0x8
    129a:	5b                   	pop    rbx
    129b:	5d                   	pop    rbp
    129c:	41 5c                	pop    r12
    129e:	41 5d                	pop    r13
    12a0:	41 5e                	pop    r14
    12a2:	41 5f                	pop    r15
    12a4:	c3                   	ret    
    12a5:	66 66 2e 0f 1f 84 00 	data16 nop WORD PTR cs:[rax+rax*1+0x0]
    12ac:	00 00 00 00 
    12b0:	f3 0f 1e fa          	endbr64 
    12b4:	c3                   	ret    

Disassembly of section .fini:

00000000000012b8 <.fini>:
    12b8:	f3 0f 1e fa          	endbr64 
    12bc:	48 83 ec 08          	sub    rsp,0x8
    12c0:	48 83 c4 08          	add    rsp,0x8
    12c4:	c3                   	ret    
