// // helper to dump arguments safely
// function dumpArg(arg) {
//     try {
//         // attempt to read as C string
//         return `"${arg.readCString()}"`;
//     } catch (_) {
//         try {
//             return hexdump(arg, { length: 32 });
//         } catch (__) {
//             return arg.toString();
//         }
//     }
// }

// function hookExport(name) {
//     const mod = Process.getModuleByName("libnative.so");
//     const addr = mod.getExportByName(name)
//     if (!addr) {
//         console.log("[!] Could not find " + name);
//         return;
//     }
//     Interceptor.attach(addr, {
//         onEnter(args) {
//             this.argsCopy = [];
//             let out = `[+] ${name}(`;
//             for (let i = 0; i < 3; i++) { // log up to 6 args
//                 try {
//                     out += dumpArg(args[i]) + ", ";
//                     this.argsCopy.push(args[i]);
//                 } catch (e) {
//                     out += args[i] + ", ";
//                 }
//             }
//             console.log(out + "...)");
//         },
//         onLeave(retval) {
//             try {
//                 let retStr = "";
//                 if (!retval.isNull()) {
//                     try {
//                         retStr = retval.readCString();
//                     } catch (_) {
//                         retStr = hexdump(retval, { length: 32 });
//                     }
//                 }
//                 console.log(`[-] ${name} => ${retStr}`);
//             } catch (e) {
//                 console.log(`[-] ${name} => ${retval}`);
//             }
//         }
//     });
//     //console.log("[*] Hooked " + name);
// }

// // list of exports to hook
// [
//   "buffer_manager",
//   "buf_util",
//   "config_loader",
//   "data_helper",
//   "force_data_preservation",
//   "get_client_version",
//   "hidden_decrypt_function",
//   "hidden_encode_function",
//   "hidden_log_function",
//   "process_data_complete",
//   "test_all_functions",
//   "util_func_a",
//   "util_func_b",
//   "util_func_c",
//   "util_func_d",
//   "version_info"
// ].forEach(hookExport);


const mod = Process.getModuleByName("libnative.so");
const base = mod.base; // 0x7a68cea000
const process_data_complete = mod.getExportByName("process_data_complete") // 0x7a68cebf6c
// 0x7a68cebf6c

Interceptor.attach(process_data_complete, {
    onEnter(args) {
        const test_input = "COUPON:XXX"
        args[0] = Memory.allocUtf8String(test_input);
        console.log(`process_data_complete(${test_input})`);
    },
    onLeave(retval) {
        retval.replace(Memory.allocUtf8String("VALID_TOKEN"));
        return;
        
        try {
            let retStr = "";
            if (!retval.isNull()) {
                try {
                    retStr = retval.readCString();
                } catch (_) {
                    retStr = hexdump(retval, { length: 32 });
                }
            }
            console.log(`[-] process_data_complete => ${retStr}`);
        } catch (e) {
            console.log(`[-] process_data_complete => ${retval}`);
        }
    }
});


// const target = ptr("0x7a75a70c60")
// console.log("[*] Hooking computeAES at", target);
// Interceptor.attach(target, {
//     onEnter(args) {
//         this.arg1 = args[0];
//         this.arg2 = args[1];
//         this.key  = args[2];
//         console.log("[+] computeAES(" +
//             "arg1=" + this.arg1.readCString() +
//             ", arg2=" + this.arg2.readCString() +
//             ", key="  + this.key.readCString() +
//         ")");
//     },
//     onLeave(retval) {
//         console.log("[-] computeAES returned:", retval.toString());
//         try {
//             // if retval is pointer to string
//             console.log("    retval as cstring:", retval.readCString());
//         } catch (_) {
//             // safe ignore if not a string
//         }
//     }
// });

/*
[Android Emulator 5554::MasterBaker ]-> mod.getExportByName("process_data_complete");
"0x7a75a6ff6c" // 0x401f6c
[Android Emulator 5554::MasterBaker ]-> mod.base
"0x7a75a6e000" // 
[Android Emulator 5554::MasterBaker ]-> ptr("0x7a75a6e000").add("0x401f6c")
"0x7a75e6ff6c"

If i rebase the address via binja: 0x7a75 e 6ff6c instead of 0x7a75 a 6ff6c

ptr("0x7a75a6ff6c").sub("0x7a75a6e000")
"0x1f6c"

diff = given - (func - base)

0x400000 = ptr("0x401f6c").sub(ptr("0x7a75a6ff6c").sub("0x7a75a6e000"))

given = diff + (func - base)

ptr("0x401f6c").sub(ptr("0x400000")).add(mod.base)

[Android Emulator 5554::MasterBaker ]-> ptr("0x401f6c").sub(ptr("0x400000")).add(mod.base)
"0x7a75a6ff6c"

0x7a75a6ff6c
*/

function hookSockets() {
    // socket(domain, type, protocol)
    Interceptor.attach(Module.findGlobalExportByName("socket"), {
        onEnter(args) {
            this.domain = args[0].toInt32();
            this.type   = args[1].toInt32();
            this.proto  = args[2].toInt32();
            console.log(`[+] socket(domain=${this.domain}, type=${this.type}, proto=${this.proto})`);
        },
        onLeave(retval) {
            console.log(`[-] socket fd=${retval.toInt32()}`);
        }
    });

    // connect(sockfd, addr, addrlen)
    Interceptor.attach(Module.findGlobalExportByName("connect"), {
        onEnter(args) {
            this.sockfd = args[0].toInt32();
            this.addr   = args[1];
            this.len    = args[2].toInt32();

            try {
                const family = Memory.readU16(this.addr);
                if (family === 2) { // AF_INET
                    const port = ((Memory.readU8(this.addr.add(2)) << 8) |
                                   Memory.readU8(this.addr.add(3)));
                    const ip   = [
                        Memory.readU8(this.addr.add(4)),
                        Memory.readU8(this.addr.add(5)),
                        Memory.readU8(this.addr.add(6)),
                        Memory.readU8(this.addr.add(7))
                    ].join(".");
                    console.log(`[+] connect(fd=${this.sockfd}) → ${ip}:${port}`);
                }
            } catch (e) {
                console.log(`[!] connect parse failed: ${e}`);
            }
        }
    });

    // // sendto(sockfd, buf, len, flags, dest_addr, addrlen)
    // Interceptor.attach(Module.findGlobalExportByName("sendto"), {
    //     onEnter(args) {
    //         const fd = args[0].toInt32();
    //         const buf = args[1];
    //         const len = args[2].toInt32();
    //         console.log(`[+] sendto(fd=${fd}, len=${len})`);
    //         if (!buf.isNull() && len > 0) {
    //             console.log(hexdump(buf, { length: Math.min(128, len) }));
    //             try {
    //                 console.log("  as string:", buf.readCString(len));
    //             } catch (_) {}
    //         }
    //     }
    // });

    // // recvfrom(sockfd, buf, len, flags, src_addr, addrlen)
    // Interceptor.attach(Module.findGlobalExportByName("recvfrom"), {
    //     onEnter(args) {
    //         this.fd  = args[0].toInt32();
    //         this.buf = args[1];
    //         this.len = args[2].toInt32();
    //     },
    //     onLeave(retval) {
    //         const n = retval.toInt32();
    //         if (n > 0) {
    //             console.log(`[+] recvfrom(fd=${this.fd}, got=${n} bytes)`);
    //             console.log(hexdump(this.buf, { length: Math.min(128, n) }));
    //             try {
    //                 console.log("  as string:", this.buf.readCString(n));
    //             } catch (_) {}
    //         }
    //     }
    // });
}

// hookSockets();


