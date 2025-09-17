

Java.perform(() => {
    const MainActivity4 = Java.use("com.example.test2.MainActivity4")
    const transformFlag = MainActivity4.transformFlag;
    transformFlag.implementation = function (flag) {
        console.log(flag);
        return transformFlag.call(this,flag);
  };
})