# 1. Jadx

I already saw `libstoreftw.so` as an ressource :D 

```bash
❯ file libstoreftw.so
libstoreftw.so: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV), dynamically linked, BuildID[sha1]=5957576da60585d36e40cd625eecddff0088bd17, stripped
```

```java
public class MainActivity extends AppCompatActivity {
    public native void storeftw();

    static {
        System.loadLibrary("storeftw");
    }

    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    protected void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        final EditText editText = (EditText) findViewById(R.id.editText);
        Button button = (Button) findViewById(R.id.buttonSaveText);
        Button button2 = (Button) findViewById(R.id.buttonStoreFlag);
        if (**RootDetection.isDeviceRooted(this)**) {
        }
    }
}
```

- There is some root detection we can sidestep with frida by hooking the `RootDetection.isDeviceRooted` method to always return `False`
- Only exported method is `storeftw` which has side effects I guess because of no arguments and return valuess

```c
  void detectDebuggers() __noreturn

      uint64_t x8 = _ReadMSR(SystemReg: tpidr_el0)
      int64_t x8_1 = *(x8 + 0x28)
      isDebuggerNotPresent = 0
      
      if (ptrace(request: PTRACE_TRACEME, 0, 0, 0) != -1)
          int128_t var_370
          char* x22_1 = &var_370 | 1
```

1. Attach to ptrace and induce a sleep

