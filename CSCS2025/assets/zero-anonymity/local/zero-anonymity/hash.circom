
pragma circom 2.0.0;

include "circomlib/circuits/bitify.circom";
include "circomlib/circuits/pedersen.circom";

template AuthToken() {
    signal input first_name;
    signal input last_name;
    signal input email;
    signal input id;
    signal output out[2];

    component first_name_bits = Num2Bits(128);
    component last_name_bits = Num2Bits(128);
    component email_bits = Num2Bits(248);
    component id_bits = Num2Bits(240);

    first_name_bits.in <== first_name;
    last_name_bits.in <== last_name;
    email_bits.in <== email;
    id_bits.in <== id;

    component hasher = Pedersen(744);
    for (var i = 0; i < 248; i++) {
        hasher.in[i+256] <== email_bits.out[i];
        if (i < 128) {
            hasher.in[i] <== first_name_bits.out[i];
            hasher.in[i+128] <== last_name_bits.out[i];
        }
        if (i < 240) {
            hasher.in[i+504] <== id_bits.out[i];
        }
    }

    out[0] <== hasher.out[0];
    out[1] <== hasher.out[1];
}

component main {public [first_name, last_name, email]} = AuthToken();