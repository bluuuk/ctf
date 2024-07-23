Java.perform(function () {
    var Debug = Java.use("android.os.Debug");

    // Hook isDebuggerConnected
    Debug.isDebuggerConnected.implementation = function() {
        console.log("Bypassing isDebuggerConnected");
        return false;
    };

    // Hook waitingForDebugger
    Debug.waitingForDebugger.implementation = function() {
        console.log("Bypassing waitingForDebugger");
        return false;
    };

    Java.use("android.os.Build").PRODUCT.value = "";
    Java.use("android.os.Build").MANUFACTURER.value = "";
    Java.use("android.os.Build").BRAND.value = "";
    Java.use("android.os.Build").DEVICE.value = "";
    Java.use("android.os.Build").MODEL.value = "";
    Java.use("android.os.Build").HARDWARE.value = "";
    Java.use("android.os.Build").FINGERPRINT.value = "";

    var pk = Java.use("com.example.mobile_challenge.pk");

    pk.hashPassword.implementation = function(pw){
        console.log("sgasd")
        return "f71fa237d00da5eadd8edb15d8abb8f7c83c492e26ce43266facb552630b2e16";
    }

});

console.log("new");