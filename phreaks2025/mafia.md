Wireshark dump

`tls.handshake.type == 1` => 
Extension: server_name (len=45) name=phishing-detection.metafi.codefi.network

`frame contains "contract"`

Response: @time=2024-06-25T20:17:36.598Z :carlo54648!~wep@freenode-n32.6hc.t6e10e.IP PRIVMSG #DarkNetMafia :The contract address is 0x69E881DB5160cc5543b544603b04908cac649D38.

Trailer: The contract address is 0x69E881DB5160cc5543b544603b04908cac649D38.

https://sepolia.etherscan.io/tx/0x22c4ea3b9dc23f8e38ced762913d0496908eed32e080b603bcc38d2c9a64516a

```
0xf6e57e600000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000003150574e4d457b3078363945383831444235313630636335353433623534343630336230343930386361633634394433387d000000000000000000000000000000
```

If I decode that to latin1, i am getting `PWNME{0x69E881DB5160cc5543b544603b04908cac649D38}` but that is an invalid flag so help me god

However, I looked at other transaction and found https://sepolia.etherscan.io/tx/0x2a1133ebd2476d670b2b1668f7db32774e02533b8ca9f2e1a98a9a67b9dd9165 which finally contains the flag :open_mouth: