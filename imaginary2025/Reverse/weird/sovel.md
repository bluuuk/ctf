 apktool d app-debug.apk -o out

 1. No special libs


Only usage here
****
```java
final String transformedFlag = MainActivity4.transformFlag("REDACTED");
```

```java
    public static final String transformFlag(String flag) {
        Intrinsics.checkNotNullParameter(flag, "flag");
        String res = "";
        int length = flag.length();
        for (int i = 0; i < length; i++) {
            int length2 = "abcdefghijklmnopqrstuvwxyz".length();
            for (int c = 0; c < length2; c++) {
                if ("abcdefghijklmnopqrstuvwxyz".charAt(c) == flag.charAt(i)) {
                    int ind = c + i;
                    res = res + "abcdefghijklmnopqrstuvwxyz".charAt(ind % "abcdefghijklmnopqrstuvwxyz".length());
                }
            }
            int length3 = "0123456789".length();
            for (int c2 = 0; c2 < length3; c2++) {
                if ("0123456789".charAt(c2) == flag.charAt(i)) {
                    int ind2 = (i * 2) + c2;
                    res = res + "0123456789".charAt(ind2 % "0123456789".length());
                }
            }
            int length4 = "!@#$%^&*()_+{}[]|".length();
            for (int c3 = 0; c3 < length4; c3++) {
                if ("!@#$%^&*()_+{}[]|".charAt(c3) == flag.charAt(i)) {
                    int ind3 = (i * i) + c3;
                    res = res + "!@#$%^&*()_+{}[]|".charAt(ind3 % "!@#$%^&*()_+{}[]|".length());
                }
            }
        }
        return res;
    }
```

![alt text](image.png)

```java
TextKt.m2712Text4IGK_g("Transformed flag: idvi+1{s6e3{)arg2zv[moqa905+", modifier3, 0L, 0L, (FontStyle) null, (FontWeight) null, (FontFamily) null, 0L, (TextDecoration) null, (TextAlign) null, 0L, 0, false, 0, 0, (Function1<? super TextLayoutResult, Unit>) null, (TextStyle) null, $composer2, i3, 0, 131068);
```

```idvi+1{s6e3()arg2zv[moqa905+```

```
❯ frida -U -F "com.example.test2" -l solve.js
     ____
    / _  |   Frida 17.2.9 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://frida.re/docs/home/
   . . . .
   . . . .   Connected to Android Emulator 5554 (id=emulator-5554)
Error: Unable to find fields in java/lang/Thread; please file a bug
```

````
❯ frida-trace -U -F "com.example.test2" -j 'com.example.test2.MainActivity*!*'
Instrumenting...                                                        
^C%           
```

ChatGPT the reverse and yeah ....