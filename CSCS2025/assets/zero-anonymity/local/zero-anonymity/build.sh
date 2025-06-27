#!/bin/bash

CIRCUIT_NAME=hash
CIRCUITJS_DIR="${CIRCUIT_NAME}_js"
POWERS_OF_TAU=14 # support 2^$POWERS_OF_TAU constraints

rm -rf "${CIRCUITJS_DIR}" *.r1cs *.sym *.json *.zkey *.wtns *.ptau

echo "Build circuit"
circom "${CIRCUIT_NAME}.circom" --r1cs --wasm --sym --inspect

echo "Write witness file"
FIRST_NAME=$(python3 -c "print(int.from_bytes('John'.encode()))")
LAST_NAME=$(python3 -c "print(int.from_bytes('Doe'.encode()))")
EMAIL=$(python3 -c "print(int.from_bytes('jdoe@trustworthy.gov'.encode()))")
RAND_ID=$(python3 -c "import secrets; print(secrets.randbelow(1 << 240))")

cat <<EOT > input.json
{"first_name": "${FIRST_NAME}", "last_name": "${LAST_NAME}", "email": "${EMAIL}", "id": "${RAND_ID}"}
EOT

echo "Generate witness"
node "${CIRCUITJS_DIR}/generate_witness.js" "${CIRCUITJS_DIR}/${CIRCUIT_NAME}.wasm" input.json witness.wtns

echo "Create new powersoftau"
snarkjs powersoftau new bn128 $POWERS_OF_TAU pot${POWERS_OF_TAU}_0000.ptau -v

echo "First contribution to powersoftau"
python3 -c "import secrets; print(secrets.token_urlsafe(128))" | snarkjs powersoftau contribute pot${POWERS_OF_TAU}_0000.ptau pot${POWERS_OF_TAU}_0001.ptau --name="Trustworthy First Contribution" -v

echo "Prepare phase 2 of powersoftau (circuit specific)"
snarkjs powersoftau prepare phase2 pot${POWERS_OF_TAU}_0001.ptau pot${POWERS_OF_TAU}_final.ptau -v

echo "Run setup for Groth16"
snarkjs groth16 setup "${CIRCUIT_NAME}.r1cs" pot${POWERS_OF_TAU}_final.ptau "${CIRCUIT_NAME}_0000.zkey"

echo "Contribute to the phase 2"
python3 -c "import secrets; print(secrets.token_urlsafe(128))" | snarkjs zkey contribute "${CIRCUIT_NAME}_0000.zkey" "${CIRCUIT_NAME}_0001.zkey" --name="John Doe (super trustworthy government official)" -v

echo "Export verification key"
snarkjs zkey export verificationkey "${CIRCUIT_NAME}_0001.zkey" verification_key.json

echo "Create Groth16 proof for circuit"
snarkjs groth16 prove "${CIRCUIT_NAME}_0001.zkey" witness.wtns proof.json public.json

echo "Verify proof"
snarkjs groth16 verify verification_key.json public.json proof.json

echo "Update server verification key"
cp verification_key.json server/