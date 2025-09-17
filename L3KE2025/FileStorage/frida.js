Java.perform(() => {
  const RootDetection = Java.use('ctf.l3akctf.filestorage.RootDetection');
  RootDetection.isDeviceRooted.implementation = function () {
    return false;
  };
});

// Interceptor.attach(Module.findGlobalExportByName("pthread_create"), {
//     onEnter(args) {
//         var module = Process.findModuleByName("libstoreftw.so") 
//         console.log(`pthread_create(${args[0]}, ${args[1]}, ${ptr(args[2]).sub(module.base)}, ${args[3]})`)
//     }
// });

/*
pthread_create(0x7afa2ebb40, 0x0, 0x33d5ea548, 0xb400007bbbc8cfd0)
pthread_create(0x7ff3214018, 0x7ff3214050, 0x81ede6d0, 0xb400007c5bccdc00)
pthread_create(0x7ff3214148, 0x7ff3214180, 0x81ede6d0, 0xb400007c5bccc030)
pthread_create(0x7ff3214678, 0x7ff32146b0, 0x81ede6d0, 0xb400007c5bcd82e0)
pthread_create(0x7a980fe698, 0x7a980fe6d0, 0x81ede6d0, 0xb400007c5bcd9eb0)
pthread_create(0x7afa2eb5e8, 0x0, 0x313ef37a8, 0xb400007b4bcbdc90)
pthread_create(0x7afa2eb7f0, 0x0, 0x33d481314, 0xb400007b4bcc3250)
pthread_create(0x7afa2eb7f0, 0x0, 0x33d481314, 0xb400007b4bcc2c50)
pthread_create(0x7afa70da30, 0x0, 0x313f25360, 0xb400007bcbccec70)
pthread_create(0x7afb5bf618, 0x7afb5bf620, 0x31750df50, 0xb400007bcbccf360)
pthread_create(0x7ff3214858, 0x7ff3214890, 0x81ede6d0, 0xb400007c5bceb4d0)
pthread_create(0x7a982f36b0, 0x0, 0x63bb0, 0x0) <- 0x63bb0 should be the adress then
Process terminated <- due to kill
*/


Interceptor.attach(Module.findGlobalExportByName("fwrite"), {
    onEnter: function(args) {
        console.log(`fwrite(${args[0]}, ${args[1]}, ${args[2]}, ${args[3]})`);
        // var size = args[1].toInt32() * args[2].toInt32();
        // var content = Memory.readUtf8String(args[0], size);
        // if (content?.includes('}')) console.log('L3AK{' + content);
    }
});

Java.perform(function() {
    setTimeout(function() {
        var module = Process.findModuleByName("libstoreftw.so");
        if (module) {
            var security_thread_addr = module.base.add(0x63bb0);
            Interceptor.attach(security_thread_addr, {
                onEnter: function(args) {
                    console.log("hi there")
                    Thread.sleep(5);
                    console.log("bye there")
                }
            });    
        }    
    }, 500);
});

// const pthread_create_ptr = Module.findGlobalExportByName("pthread_create");
// const pthread_create_orig = new NativeFunction(pthread_create_ptr, "int",
//                                 ["pointer","pointer","pointer","pointer"]);

// const replacement = new NativeCallback(() => {
//         console.log("I am waiting")
//         Thread.sleep(100);
//         return ptr(0);
//       }, 'pointer', []);

// setTimeout(() => {
// Interceptor.replace(pthread_create_ptr, new NativeCallback((tidPtr, attrPtr, start, arg) => {
//   console.log("pthread_create start:", start);
//   if (Process.getModuleByName("libstoreftw.so")) {
//     const base = Process.getModuleByName("libstoreftw.so").base;
//     if (start.equals(base.add(0x63bb0))) {
//       console.log("Redirecting start routine");
//       start = replacement
//     }
//   }
//   return pthread_create_orig(tidPtr, attrPtr, start, arg);
// }, 'int', ['pointer','pointer','pointer','pointer']));
// },300)

// const ptrace = Module.findGlobalExportByName("ptrace");
// const kill = Module.findGlobalExportByName("kill");
// const open = Module.findGlobalExportByName("open");
// const stat = Module.findGlobalExportByName("stat");
// const strstr = Module.findGlobalExportByName("strstr");
// const dlopen = Module.findGlobalExportByName("dlopen");
// const socket = Module.findGlobalExportByName("socket");
// const dlsym = Module.findGlobalExportByName("dlsym");
// const opendir = Module.findGlobalExportByName("opendir");


// // dlsym(handle: handle_2, name: "frida_agent_main")
// // Interceptor.attach(dlsym, {
// //     onEnter(args) {
// //         console.log(`dlsym(${args[0]}, ${args[1].readUtf8String()})`);
// //     }
// // });


// /*
// dlopen(libfrida-gum.so, 0x6)
// dlopen(libfrida-agent.so, 0x6)
// dlopen(libfrida.so, 0x6)
// dlopen(libgum-js-loop.so, 0x6)
// dlopen(libgmain.so, 0x6)
// dlopen(liblinjector.so, 0x6)
// */

// // dlopen(file: &var_770, mode: 6)
// setTimeout(function(){
//     Interceptor.attach(dlopen, {
//         onEnter(args) {
//             const needle = args[0].readUtf8String()
//             console.log(`dlopen(${needle}, ${args[1]})`);

//             if(needle.includes("frida") || needle.includes("gum")){
//                 this.shouldModify = true
//             }
//         }, onLeave(ret) {
//             if (this.shouldModify){
//                 ret.replace(0)
//             }
//     }
//     })
// },
// 3000
// )

// setTimeout(function(){
// Interceptor.attach(open, {
//     onEnter(args) {
//         const file = args[0].readUtf8String()
//         console.log(`open(${file}, ${args[1]})`);
//         if(file.includes("/proc/")){
//             this.shouldModify = true
//         }
//     }, onLeave(ret) {
//         if (this.shouldModify){
//             ret.replace(0)
//         }
//     }
// })},
// 3000
// )

// // Interceptor.attach(Module.findGlobalExportByName("fopen64"), {
// //   onEnter(args) {
// //     const file = args[0].readUtf8String();
// //     console.log(`fopen64(${file}, ${args[1].readUtf8String()})`);
// //     if (file.includes("/proc/")) {
// //        this.shouldModify = true;
// //     }
// //   },
// //   onLeave(ret) {
// //     if (this.shouldModify) ret.replace(ptr(0));
// //   }
// // });

// const fopen64ptr = Module.findGlobalExportByName("fopen64");
// const fopen64 = new NativeFunction(fopen64ptr, 'int', ['pointer', 'pointer']);

// Interceptor.replace(fopen64ptr, new NativeCallback((file,mode) => {
//     const target = file.readUtf8String()
//     if (target.includes("/proc/")){
//         return 0;
//     }else{
//         return fopen64(target,mode);
//     }
// }, 'int', ['pointer', 'pointer']));


// const usleep = Module.findGlobalExportByName("usleep");
// // usleep(useconds: 0x14)
// Interceptor.attach(usleep, {
//     onEnter(args) {
//         args[0] = ptr(1000000);
//     },
// });


// // connect(fd: socket, addr: &var_770, len: 0x10)
// // Interceptor.attach(connect, {
// //     onEnter(args) {
// //         console.log(`connect(${args[0]}, ${args[1]}, ${args[2]})`);
// //     }
// // });

// Interceptor.attach(stat, {
//     onEnter(args) {
//         const target = args[0].readUtf8String()
//         console.log(`stat(${args[0].readUtf8String()}, ${args[1]})`);
//     }
// });

// Interceptor.attach(socket, {
//     onEnter(args) {
//         // if ((socket & 0x80000000) == 0)
//         console.log(`socket(${args[0]}, ${args[1]}, ${args[2]})`);
//     }
// });

// Interceptor.attach(opendir, {
//     onEnter(args) {
//         // DIR* opendir(char const* name)
//         const target = args[0].readUtf8String()
//         console.log(`opendir(${target})`);
//         if (target.includes("proc") || target.includes("tmp")){
//             this.shouldModify = true
//         }
//     }, onLeave(ret) {
//         if (this.shouldModify){
//             ret.replace(0)
//         }
//     }
// });



// const targets = {
//     "frida" : true,
//     "frida-agent" : true,
//     "frida-gum" : true,
//     "frida-server" : true,
//     "gadget" : true,
//     "gmain" : true,
//     "gum-js-loop" : true,
//     "hluda" : true,
//     "hluda-server" : true,
//     "linjector" : true,
// }

// Interceptor.attach(strstr, {
//     onEnter(args) {
//         this.shouldModify = args[1].readUtf8String() in targets;
//     },
//     onLeave(ret) {
//         if (this.shouldModify){
//             ret.replace(0)
//         }
//     }
// });

// Interceptor.attach(ptrace, {
//     onEnter(args) {
//         console.log(`ptrace(${args[0]}, ${args[1]}, ${args[2]}, ${args[3]})`);
//     },
//     onLeave(ret) {
//         ret.replace(0);
//     }
// });


// /*
//       if (pthread_create(&thread, 0, detectDebuggers, 0) == 0)
//           pthread_detach(thread)
//           startedThreat = 1

// ----

// Interceptor.attach(Module.findGlobalExportByName("pthread_detach"), {
//     onEnter(args) {
//         // extern size_t fwrite(void const* buf, size_t size, size_t count, FILE* fp)
//         // https://en.cppreference.com/w/c/io/fwrite -> size == size of object, count == number of objects
//         console.log(`pthread_detach(${args[0]})`)
//     }
// });



// pthread_create(0x7b1a815f78, 0x0, 0x7b19ffd01c, 0xb400007ccbcc2650)
// pthread_create(0x7ff3214958, 0x7ff3214960, 0x7daf722f50, 0xb400007bcbcb7c30)
// pthread_create(0x7ff3214ae0, 0x0, 0x7dbc4d48e0, 0xb400007bbbc8f4d0)
// pthread_detach(0x7aa51fdcb0)
// pthread_create(0x7afa319b40, 0x0, 0x7dd57ff548, 0xb400007bbbc8ecf0)
// pthread_detach(0x7aa51fdcb0)
// pthread_create(0x7ff3214018, 0x7ff3214050, 0x7b1a0f36d0, 0xb400007c5bccdc00)
// pthread_create(0x7ff3214148, 0x7ff3214180, 0x7b1a0f36d0, 0xb400007c5bccc030)
// pthread_create(0x7ff3214678, 0x7ff32146b0, 0x7b1a0f36d0, 0xb400007c5bcd82e0)
// pthread_create(0x7a981ea698, 0x7a981ea6d0, 0x7b1a0f36d0, 0xb400007c5bcd9eb0)
// pthread_create(0x7afa3195e8, 0x0, 0x7dac1087a8, 0xb400007b4bcbdc90)
// pthread_detach(0x7a97dcecb0)
// pthread_create(0x7afa3197f0, 0x0, 0x7dd5696314, 0xb400007b4bcc3250)
// pthread_detach(0x7a97cd0cb0)
// pthread_create(0x7afa3197f0, 0x0, 0x7dd5696314, 0xb400007b4bcc2c50)
// pthread_detach(0x7a97bd2cb0)
// pthread_create(0x7afa746a30, 0x0, 0x7dac13a360, 0xb400007bcbccec10)
// pthread_create(0x7afa747618, 0x7afa747620, 0x7daf722f50, 0xb400007bcbccb610)
// pthread_create(0x7ff3214858, 0x7ff3214890, 0x7b1a0f36d0, 0xb400007c5bceb4d0)
// pthread_create(0x7ff3214918, 0x7ff3214950, 0x7b1a0f36d0, 0xb400007c5bcb1f00)
// pthread_create(0x7a983df6b0, 0x0, 0x7a98364bb0, 0x0)
// pthread_detach(0x7afdb5ccb0)

// ----

// pthread_create(0x7a983e86b0, 0x0, 0x7a9836dbb0, 0x0)
// pthread_detach(0x7afd794cb0)

// 0x464c8c - 0x463bb0 - 0x463bb0
// */


// // setTimeout(() => {
// //     const storeBase = Process.getModuleByName("libstoreftw.so").base;
// //     const fctPtr = storeBase.add(0x63bb0);

// //     Interceptor.replace(fctPtr, new NativeCallback(() => {
// //             console.log("here");
// //         }
// //     , "void", []));
// // }, 2000);

// // Interceptor.attach(Module.findGlobalExportByName("pthread_create"), {
// //   onEnter(args) {
// //     const objptr     = args[0];
// //     const attrPtr     = args[1];
// //     const startRoutine = args[2];
// //     const argPtr      = args[3];
// //     console.log(`pthread_create(obj=${objptr}, attr=${attrPtr}, start=${startRoutine}, arg=${argPtr})`);
    
// //     try {
// //         const storeBase = Process.getModuleByName("libstoreftw.so").base;
// //         if (startRoutine.equals(storeBase.add(0x63bb0))) {
// //             args[2] = new NativeCallback(() => {
// //                 Thread.sleep(1000);
// //             },'void',[])
// //             console.log(`!! Redirecting start_routine → ${args[2]}`);
// //         }
// //     } catch (error) {
// //         console.log("not yet loaded")        
// //     }
// //   }
// // });


// // this sadly crashes the application as the frida debugger has apparently some inbuild assertions that the detection script is running

// /*
// const pthread_create_ptr = Module.findGlobalExportByName("pthread_create");
// const pthread_create = new NativeFunction(pthread_create_ptr, 'int', ['pointer', 'pointer', 'pointer', 'pointer']);

// // Our custom callback
// var test = new NativeCallback(() => {
//     Thread.sleep(1);
//     console.log("i got called")
// }, 'void', ['pointer']);

// Interceptor.replace(pthread_create_ptr, new NativeCallback((thread, attr, start_routine, arg) => {
//     try {
//         const storeBase = Process.getModuleByName("libstoreftw.so").base;
//         const targetRoutine = storeBase.add(0x63bb0);

//         if (start_routine.equals(targetRoutine)) {
//             console.log(`[*] Intercepted pthread_create with target start_routine: ${start_routine}`);
//             return pthread_create(thread, attr, test, arg);
//         }
//     } catch (e) {
//         // libstoreftw.so not loaded yet
//     }

//     // Default behavior
//     return pthread_create(thread, attr, start_routine, arg);
// }, 'int', ['pointer', 'pointer', 'pointer', 'pointer']));
// */

