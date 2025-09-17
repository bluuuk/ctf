Java.perform(function() {
    const api = Java.use("com.sekai.bank.network.ApiClient")
    console.log(api)

    api.getFlag()
});
