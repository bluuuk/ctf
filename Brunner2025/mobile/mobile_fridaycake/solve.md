
#

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

`getDecryptedFlag` is not used tho :( => Frida


![alt text](image.png)

```javascript
Java.perform(() => {
    var checker = Java.use("dk.brunnerctf.fridaycake.NativeChecker");
    var checkerInstance = checker.$new();
    var result = checkerInstance.getDecryptedFlag();
    console.log("Flag: " + result);
})
```