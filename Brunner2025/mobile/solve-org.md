# mobile_rivalcakes(easy)

Given this challenge description and a file dump, we need to find a password and a location:

```
The secret Brunner and Othello cults are waging their battles in the streets of Denmark.

One day, you see a member of the Othello cult drop their phone out of their pocket. You grab it, but it seems to be a burner phone. You find only two custom apps, but when opening one, it instantly deletes itself - maybe there is still some data left?

In the cake cults, preferences matter - so keep an eye out and mind what you say.

Your Othello rivals are planning a secret meetup, find out where and find the password to infiltrate them!

Flag format: The flag is formatted as brunner{<w3w_code>_<password>}, where <w3w_code> is the what3words code of the location, without leading slashes. Make sure your "3 word address language" is set to English.
```

While clicking through the files, I quickly found `data/data/dk.brunnerctf.rivalcakes` which matches the challenge description. An inital check for `password`, `loc`, `lat` did not bring anything. I first tried to get an overview:

```bash
❯ tree .
.
├── app_textures
├── app_webview
│   ├── Default
│   │   ├── blob_storage
│   │   │   └── ac572a83-ec69-47ee-8bb1-6a8869725a84 <- INTERESTING
│   │   ├── Local Storage
│   │   │   └── leveldb
│   │   │       ├── 000005.log
│   │   │       ├── CURRENT
│   │   │       ├── LOCK
│   │   │       ├── LOG
│   │   │       ├── LOG.old
│   │   │       └── MANIFEST-000004
│   │   ├── PersistentOriginTrials
│   │   │   ├── LOCK
│   │   │   ├── LOG
│   │   │   └── LOG.old
│   │   ├── Shared Dictionary
│   │   │   ├── cache
│   │   │   │   ├── index
│   │   │   │   └── index-dir
│   │   │   │       └── the-real-index
│   │   │   ├── db
│   │   │   └── db-journal
│   │   ├── shared_proto_db
│   │   │   ├── 000005.log
│   │   │   ├── CURRENT
│   │   │   ├── LOCK
│   │   │   ├── LOG
│   │   │   ├── LOG.old
│   │   │   ├── MANIFEST-000004
│   │   │   └── metadata
│   │   │       ├── 000005.ldb
│   │   │       ├── 000006.log
│   │   │       ├── CURRENT
│   │   │       ├── LOCK
│   │   │       ├── LOG
│   │   │       ├── LOG.old
│   │   │       └── MANIFEST-000004
│   │   ├── Web Data
│   │   └── Web Data-journal
│   ├── last-exit-info
│   └── webview_data.lock
├── cache
│   ├── Crash Reports
│   │   └── ANR Variations
│   │       └── b65c4b12d7782aaf3ebc0b927a63a2b9 <- INTERESTING
│   └── WebView
│       ├── Crash Reports
│       ├── Crashpad
│       │   ├── attachments
│       │   ├── completed
│       │   ├── new
│       │   └── pending
│       ├── Default
│       │   └── HTTP Cache
│       │       └── Code Cache
│       │           ├── js
│       │           │   ├── index
│       │           │   └── index-dir
│       │           │       └── the-real-index
│       │           └── wasm
│       │               ├── index
│       │               └── index-dir
│       │                   └── the-real-index
│       ├── font_unique_name_table.pb
│       └── SafeBrowsing
├── code_cache
├── databases
│   ├── orders.db <- INTERESTING
│   ├── orders.db-journal
│   ├── orders.db-shm
│   └── orders.db-wal
├── files
│   ├── menu_temp.html
│   └── profileInstalled <- INTERESTING
└── shared_prefs
    ├── my_prefs.xml <- INTERESTING
    └── WebViewChromiumPrefs.xml
```

After seeing this, I first tried to look at the database `orders.db`. `file` told me it is an SQLite database.

```bash
sqlite> open orders.db;
sqlite> select * FROM orders limit 100;
15|Customer15|note 15|cancelled|2025-07-07 10:03:00
16|Alice|Extra frosting|delivered|2025-08-10 14:32:11
17|Bob|Meet at location in EXIF|pending|2025-08-11 09:21:44
18|Claire|part1:Othello_is_|cancelled|2025-08-12 08:59:02
20|Customer20|note 20|delivered|2025-07-03 10:02:00
```

1. `Meet at location in EXIF` $\implies$ There are images that have the location for the w3w code inside its EXIF metadata
2. Flags have parts, here `part1:Othello_is_`

As we have `part1`, I scanned with ripgrep(srly an amazing tool!!!) for others

```bash
❯ rg -e "part\d"
data/data/dk.brunnerctf.rivalcakes/files/menu_temp.html
1:<html><body><p>part4:Brunsviger</p></body></html>

data/data/dk.brunnerctf.rivalcakes/shared_prefs/my_prefs.xml
4:    <string name="step2_data">part2:always_better_</string>
```

Nice, so there is likely one part, i.e. `part3`, missing. Checking `data/data/dk.brunnerctf.rivalcakes/shared_prefs/my_prefs.xml`, we even see a path to an image:

```xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="recipe_file">/storage/emulated/0/Download/Cakes/best_cake_in_the_world.jpg</string>
    <string name="step2_data">part2:always_better_</string>
</map>
```

Let's check that image with `exiftool` and hope for the best:

```
❯ exiftool best_cake_in_the_world.jpg
======== best_cake_in_the_world.jpg
ExifTool Version Number         : 13.30
File Name                       : best_cake_in_the_world.jpg
Directory                       : .
File Size                       : 35 kB
File Modification Date/Time     : 2025:08:20 09:35:41-04:00
File Access Date/Time           : 2025:08:23 14:06:28-04:00
File Inode Change Date/Time     : 2025:08:23 14:06:25-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0232
Components Configuration        : Y, Cb, Cr, -
User Comment                    : part3:Than_an_ugly_
Flashpix Version                : 0100
Color Space                     : Uncalibrated
GPS Version ID                  : 2.3.0.0
GPS Latitude Ref                : North
GPS Longitude Ref               : East
Image Width                     : 584
Image Height                    : 194
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 584x194
Megapixels                      : 0.113
GPS Latitude                    : 55 deg 40' 29.56" N
GPS Longitude                   : 12 deg 33' 52.40" E
GPS Position                    : 55 deg 40' 29.56" N, 12 deg 33' 52.40" E
```

In there, we have `part3` and a gps location which we just translate with the given website to the code: `55° 40' 29.56" N, 12° 33' 52.40" E` $\implies$ scarred.marble.improving

> brunner{scarred.marble.improving_Othello_is_always_better_Than_an_ugly_Brunsviger}

# mobile_fridaycake(medium)

Challange along an APK given to us:

```
It's Friday - your family cake night! 🍰 But when you try to order your favorite cake, you find that someone has changed the app and locked the ordering screen!

Recover the Secret Access Code and save the family's cake tradition.
```
I quickly installed the APK via drag and drop into my Android Studio emulator to see what we are up against:

![MainActivityScreen](image.png)

However, we need to actually look at the code to see how we can get past this. My first tool to look at APKs is [JADX](https://github.com/skylot/jadx). Then I navigate to `AndroixManifest.xml` in the `Resources` tab to discover the starting point into the APK, which is also called the `MainActivity`. It is `dk.brunnerctf.fridaycake.MainActivity` which brings me to:

```java
    public static final void onCreate$lambda$0(EditText editText, MainActivity mainActivity, View view) {
        if (Authenticator.INSTANCE.checkCode(editText.getText().toString())) {
            Toast.makeText(mainActivity, "✅ Cake unlocked! Enjoy your Friday! 🎂", 1).show();
        } else {
            Toast.makeText(mainActivity, "❌ Wrong code! No cake for you...", 0).show();
        }
    }
```

The `Authenticator.INSTANCE` seems like an obvious spot to check. We see the function `checkCode` which in turn calls `NativeChecker.INSTANCE.verifyCode(...)`

```java
    public final boolean checkCode(String input) {
        Intrinsics.checkNotNullParameter(input, "input");
        String str = StringsKt.reversed((CharSequence) input).toString() + "::CAKE::";
        ArrayList arrayList = new ArrayList(str.length());
        for (int i = 0; i < str.length(); i++) {
            arrayList.add(Character.valueOf((char) (str.charAt(i) + 2)));
        }
        return NativeChecker.INSTANCE.verifyCode(CollectionsKt.joinToString$default(arrayList, "", null, null, 0, null, null, 62, null));
    }
```

Let's continue and click on `NativeChecker` to get to a sink for now:

```java
public final class NativeChecker {
    public static final NativeChecker INSTANCE = new NativeChecker();

    public final native String getDecryptedFlag();

    public final native boolean verifyCode(String code);

    private NativeChecker() {
    }

    static {
        System.loadLibrary("native-lib");
    }
}
```

The two functions in the `NativeChecker` are implmented via an `JNI` interface where Java will call a compiled library. The libraray `native-lib` is also shipped, we just have to look at the file path `Resources/lib/<Architecture>/libnative-lib.so`. I actually did not bother to continue to reverse engineer here, because there is a function `getDecryptedFlag` I would like to call first. This is a perfect use case for [frida](https://frida.re/), which is a dynamic instrumentation toolkit. It allows us to inject a javascript interpreter into a process(here the APK running on the emulator) and modify it. **DISCLAMER**: You need to click the button `Unlock Cake` once as Java lazy loads the library!

```bash
[Android Emulator 5554::FridayCake ]->
    Java.perform(() => {
        var checker = Java.use("dk.brunnerctf.fridaycake.NativeChecker"); // Class reference
        var checkerInstance = checker.$new(); // Create a new object
        var result = checkerInstance.getDecryptedFlag(); // Get our flag
        console.log("Flag: " + result);
    })
Flag: brunner{Y0u_Us3d_Fr1d4_F0r_Gr4bb1ng_Th1s_R1ght?}
[Android Emulator 5554::FridayCake ]->
```

# mobile_brod-and-co(hard)

Challange along an APK given to us:

```
Brød & Co. just released their new ordering app, but their prices are a bit high. If only I had a coupon code...

Note: The app sometimes crashes when clicking "Place Order". If this happens, try again or try another approach.
```

As with the previous challenge, we start with JADX. All we get from the `MainActivity` is that we are now stuck with flutter:

```java
package dk.brunnerne.masterbaker;

import io.flutter.embedding.android.FlutterActivity;

/* loaded from: classes.dex */
public final class MainActivity extends FlutterActivity {
}
```

I have no clue about flutter, so naturally I did something else first :D I later came back to the challenge to understand what flutter is and how we can overcome the hurdle:

1. Flutter Apps are written in Dark and depending on the compliation mode, compiled to bare metal code.
2. We have an AOT Snapshort for Android Arch64. The file `lib/arm64-v8a/libapp.so` contains the compilation flags, aka `product no-code_comments no-dwarf_stack_traces_mode dedup_instructions no-tsan no-msan arm64 android compressed-pointers`

I was reading and watching these resources:

https://blog.tst.sh/reverse-engineering-flutter-apps-part-1
https://www.guardsquare.com/blog/current-state-and-future-of-reversing-flutter-apps
https://www.youtube.com/watch?v=JNoEUPlgcZk

The last [link](https://youtu.be/JNoEUPlgcZk?feature=shared&t=2160) points out when we can disassemble the app. However, I first tried to understand why we have the library `libnative.so` which is not usual for flutter, as they only ship `libapp.so` and `libnative.so`.

## Jumping into `libnative.so`

First, I had a look if there is anything imporant for us:

```bash
❯ strings libnative.so | rg -i flag
FLAG:
FLAG|%s
FLAG|INVALID_COUPON
```

Okay nice. I wouls suspect that the library is called form flutter via a native mechanism. Let's see what methods are exported:

```bash
❯ nm -D libnative.so | grep "T"
0000000000002934 T buffer_manager
00000000000028d4 T buf_util
0000000000002978 T config_loader
00000000000028e4 T data_helper
0000000000002988 T force_data_preservation
00000000000024e0 T get_client_version
0000000000002694 T hidden_decrypt_function
00000000000024ec T hidden_encode_function
00000000000025b4 T hidden_log_function
0000000000001f6c T process_data_complete
0000000000002a9c T test_all_functions
0000000000002768 T util_func_a
00000000000027bc T util_func_b
0000000000002810 T util_func_c
00000000000028c8 T util_func_d
000000000000297c T version_info
```

Okay bad, where do we start? My first instinct is to actually verify that some functions are called form the libraray. We can do this with `frida-trace` that tells us which functions were called (*Make sure to use the app first so the libs are loaded!*):

```bash
❯ frida-trace -UF -i 'libnative.so!*'
 ... instrumenting ... 
 17221 ms  process_data_complete(COUPON:test)
```

Okay so let's look there! I already added comments for futher functions. I opted to use the `High Level IL` instead of `Pseudo C` as the if conditions confuse me.

```c
char* process_data_complete(char* coupon){
    // Normal use case via `Check Coupon`
    if (strncmp(coupon, "COUPON:", 7) == 0)
    {
        if (SomeDecryption(&coupon[7]) == 0)
            return strdup("INVALID_COUPON");
        
        return strdup("VALID_COUPON");
    }
    
    // Special case: Starts not with "FLAG:" (i.e. intended way is to submit a valid coupon request?)
    if (strncmp(coupon, "FLAG:", 5) != 0)
    {
        // seems like a hash/encryption algorithm that checks for H/E(x) == 0x5a7c2b19
        if (checkcoupon(coupon) != 0)
        {
            magic();
            char* x0_20 = malloc(__strlen_chk(&emptybuffer, -1) + 0x10);
            
            if (x0_20)
            {
                int64_t x0_21;
                int128_t v0_2;
                int128_t v1_2;
                int128_t v2_2;
                int128_t v3_2;
                int128_t v4_2;
                int128_t v5_2;
                int128_t v6_2;
                int128_t v7_2;
                x0_21 = __strlen_chk(&emptybuffer, -1);
                sub_7a68ceb99c(x0_20, -1, x0_21 + 0x10, "OK|%s", &emptybuffer, v0_2, v1_2, v2_2, 
                    v3_2, v4_2, v5_2, v6_2, v7_2);
                return x0_20;
            }
        }
        
        // this opens a socket where data is send and received from
        return sendandreceivefromlocalhost(coupon);
    }
    
    // Other way, the string XXXXXhere_is_the_input with XXXXX != "FLAG:"
    if (SomeDecryption(&coupon[5]))
    {
        magic();
        char* x0_12 = malloc(__strlen_chk(&emptybuffer, -1) + 0x10);
        
        if (x0_12)
        {
            int64_t x0_13;
            int128_t v0_1;
            int128_t v1_1;
            int128_t v2_1;
            int128_t v3_1;
            int128_t v4_1;
            int128_t v5_1;
            int128_t v6_1;
            int128_t v7_1;
            x0_13 = __strlen_chk(&emptybuffer, -1);
            sub_7a68ceb99c(x0_12, -1, x0_13 + 0x10, "FLAG|%s", &emptybuffer, v0_1, v1_1, v2_1, 
                v3_1, v4_1, v5_1, v6_1, v7_1);
            return x0_12;
        }
    }
    return strdup("FLAG|INVALID_COUPON");
}
```

Let's build a decision tree:

1. Input start with `COUPON:` 
    - Some decryption evaluates to $0$ $\implies$ `INVALID_COUPON`
2. Input does not start with `FLAG:`
    - Some hash over the input and if that has a certain value, we call `magic()` and pass its output to a function
3. Some decrpytion magic of the coupon starting at the 5th digit.
    - Call `magic()` and pass its output to a function

This doesn't look good at all. We have some decryption/hash functions that somehow make our life harder. I actually copied the code of `magic` into chatGPT which told me that its some kind of AES decryption. However, a small peak shows an important hint:

```c 
int64_t magic(){
    void var_28
    void* var_c0 = &var_28
    void* var_b8 = &emptybuffer
    
    if (callOnce == 0)
        /*
            Loops and bitmagic removed
        */
        __memcpy_chk(dstpp: &emptybuffer, srcpp: srcpp_1, len: 0x2c, dstlen: 0x40)

        *(var_b8 + 0x2c) = 0
        int32_t var_a8_1 = 0
        
        for (int32_t i_3 = 0; i_3 s< 0x2c; i_3 += 1)
            if (zx.d(*(&emptybuffer + sx.q(i_3))) s>= 0x20
                    && zx.d(*(&emptybuffer + sx.q(i_3))) s<= 0x7e)
                int64_t x10_36 = sx.q(var_a8_1)
                var_a8_1 = x10_36.d + 1
                *(&emptybuffer + x10_36) = *(&emptybuffer + sx.q(i_3))
        
        *(&emptybuffer + sx.q(var_a8_1)) = 0
        callOnce = 1
    
    return &emptybuffer
}
```

Based on the function, I thought its initalizing `emptybuffer` only time and reusing the buffer later via `callOnce`. This seems interesting because the buffer is later used for the flag! But first, we need to understand what `sub_7a68ceb99c` does in our snippet:

```c
    if (SomeDecryption(&coupon[5]))
    {
        magic();
        char* x0_12 = malloc(__strlen_chk(&emptybuffer, -1) + 0x10);
        
        if (x0_12)
        {
            int64_t x0_13;
            int128_t v0_1;
            int128_t v1_1;
            int128_t v2_1;
            int128_t v3_1;
            int128_t v4_1;
            int128_t v5_1;
            int128_t v6_1;
            int128_t v7_1;
            x0_13 = __strlen_chk(&emptybuffer, -1);
            sub_7a68ceb99c(x0_12, -1, x0_13 + 0x10, "FLAG|%s", &emptybuffer, v0_1, v1_1, v2_1, v3_1, v4_1, v5_1, v6_1, v7_1);
            return x0_12;
        }
    }
```

The function does not look complete at all:

```c
// sub_7a68ceb99c(x0_12, -1, x0_13 + 0x10, "FLAG|%s", &emptybuffer, v0_1, v1_1, v2_1, v3_1, v4_1, v5_1, v6_1, v7_1);
uint64_t sub_7a68ceb99c(char* arg1, size_t arg2, size_t arg3, char* arg4, int64_t arg5, int128_t arg6 @ v0, int128_t arg7 @ v1, int128_t arg8 @ v2, 
int128_t arg9 @ v3, int128_t arg10 @ v4, int128_t arg11 @ v5, int128_t arg12 @ v6, int128_t arg13 @ v7){
    int128_t var_b0 = arg13
    int128_t var_c0 = arg12
    int128_t var_d0 = arg11
    int128_t var_e0 = arg10
    int128_t var_f0 = arg9
    int128_t var_100 = arg8
    int128_t var_110 = arg7
    int128_t var_120 = arg6
    int64_t x7
    int64_t var_88 = x7
    int64_t x6
    int64_t var_90 = x6
    int64_t x5
    int64_t var_98 = x5
    int64_t var_a0 = arg5
    int32_t var_34 = 0xffffff80
    int32_t var_38 = 0xffffffe0
    int128_t var_80
    int128_t* var_48 = &var_80
    int128_t var_70 = (&var_a0).o
    void arg_0
    var_80 = (&arg_0).o
    // nt __vsnprintf_chk(char * s, size_t maxlen, int flag, size_t slen, const char * format, va_list args);
    return zx.q(__vsnprintf_chk(s: arg1, maxlen: arg3, flag: 0, slen: arg2, format: arg4))
}
```

The documentation for [`__vsnprintf_chk`](https://refspecs.linuxbase.org/LSB_4.1.0/LSB-Core-generic/LSB-Core-generic/libc---vsnprintf-chk-1.html) tells us that `s` is output buffer, `format` is the `printf` style format and all arguments after are `variable arguments`. I assume that due to the `variable arguments`, everything is placed on the step, which goes lost during decompilation. However, we have enough to play mix and match:

```
            char* x0_12 = malloc(__strlen_chk(&emptybuffer, -1) + 0x10);
                     |
                     |        x0_13 = __strlen_chk(&emptybuffer, -1);
                     |          |
    sub_7a68ceb99c(x0_12, -1, x0_13 + 0x10, "FLAG|%s", &emptybuffer, v0_1, v1_1, v2_1, v3_1, v4_1, v5_1, v6_1, v7_1);
                     |     |            |        |
                     |     |            |        |--------------------|
                     |     |            |                             |  
                     |     |------------|---------------|             |
                     |                  |               |             |
                     |             |----|               |             |  
                     |             |                    |             |  
__vsnprintf_chk(s: arg1, maxlen: arg3, flag: 0, slen: arg2, format: arg4)
```

When we look at `v0_1` to `v7_1`, we notice that all of them are uninitalized. The only argument is actually `&emptybuffer` which should then contain our flag! Our battleplan now would be to call `magic()` and then simply read the `emptybuffer`. As this seems like much work, there is somehow an exported function that does the job for us in the binary:

```c
int64_t buf_util(){
    magic()
    return &emptybuffer
}
```

Okay, we can easily call this with frida! To call a function, we need to the following steps:

1. Get the signature of the function such that we can call a `NativeFunction(adr,return_type,[argument_type])`
2. Get the current in memory address of the module 
3. Rebase in binja everything to the module address(makes copying the function address easy)
4. Go the the function in binja and copy the address
5. Run

```bash
[Android Emulator 5554::MasterBaker ]-> Process.getModuleByName("libnative.so").base
"0x7a68cea000"
[Android Emulator 5554::MasterBaker ]-> var buf_util = new NativeFunction(ptr(0x7a68cec8d4),"pointer",[]);
[Android Emulator 5554::MasterBaker ]-> var res = buf_util();
[Android Emulator 5554::MasterBaker ]-> res.readCString();
"brunner{wh0_kn3w_dart_c0u1d_h4nd13_C?!}"
```

This feels to easy :D

## Collection of failed ideas

### Returning `VALID_TOKEN`

Let's test what happens when the functions return `VALID_TOKEN`. With `frida-trace`, we also have the ability to intercept function in a web interface:

```bash
>  frida-trace -UN dk.brunnerne.masterbaker -i 'libnative.so!*'
Started tracing 16 functions. Web UI available at http://localhost:61491/
```

So instead of an `INVALID_TOKEN`, we just make it valid :D

```js
defineHandler({
  onEnter(log, args, state) {
    log(`process_data_complete(${args[0].readCString()})`);
  },

  onLeave(log, retval, state) {
    retval.replace(Memory.allocUtf8String("VALID_TOKEN"));
  }
});
```

Mhhhh, now we are getting a completly new input to the function

```bash
153592 ms  process_data_complete(COUPON:test2)
155898 ms  process_data_complete({"customer":{"name":"test1","timestamp":1756072657835},"order":{"items":[{"name":"Brunsviger Slice","price":25,"quantity":1,"total":25},{"name":"Cinnamon Roll","price":20,"quantity":1,"total":20},{"name":"Rye Bread Loaf","price":30,"quantity":1,"total":30}],"total":75,"note":"test3"},"metadata":{"app_version":"1.0.0","platform":"android","client_version":"network_client v1.0"}})
```

But it looks like there is actually no path in the `process_data_complete` that parses json?

### Rewriting the input to `process_data_complete`

The second if asks that input does not start with `FLAG` as in `if (strncmp(coupon, "FLAG:", 5) != 0)`. Therfore, we adjust the above defined handler to intecept the only argument to `process_data_complete`.


```js
defineHandler({
  onEnter(log, args, state) {
    args[0] = Memory.allocUtf8String("TEST")
    log(`process_data_complete(${args[0].readCString()})`);
  },

  onLeave(log, retval, state) {
    log(`process_data_complete() -> ${retval.readCString()}`);
  }
});
```

I kept receiving `ERROR: Connection failed` which totally confused me. However, this was not a frida error which I errornosly belived first. Going into the code of `sendandreceivefromlocalhost`, we have a call to `socket` and `connect`. The socket call is, however, not allowed as the permision `<uses-permission android:name="android.permission.INTERNET"/>` is missing. My idea then was to take the APK and add the permission:

1. Destruct the APK via `apktool d <file>`
2. Add permission to `AndroixManifest.xml`
3. Resign and realign with [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer): `java -jar uber-apk-signer-1.3.0.jar --allowResign -a masterbaker/dist/MasterBaker.apk`

When I opened a shell via `adb`, I recevied gibberish via `nc -s 127.0.0.1 -p 8088 -l`. I stopped working on this as I focused more on the `magic` method.
