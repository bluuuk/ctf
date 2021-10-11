package main

import (
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"encoding/hex"
	"fmt"
	"log"
	"math/rand"
	"sync"
)

var flag string
var flagmu sync.Mutex

/*

func PKCS5Padding(ciphertext []byte, blockSize int, after int) []byte {
	padding := (blockSize - len(ciphertext)%blockSize)
	padtext := bytes.Repeat([]byte{byte(padding)}, padding)
	return append(ciphertext, padtext...)
}


func decrypt(ciphertext, bKey, bIV, prefix []byte, blockSize int) string {
	bPlaintext := PKCS5Padding([]byte(plaintext), blockSize, len(plaintext))
	block, err := aes.NewCipher(bKey)
	if err != nil {
		log.Println(err)
		return ""
	}
	ciphertext := make([]byte, len(bPlaintext))
	mode := cipher.NewCBCEncrypter(block, bIV)
	mode.CryptBlocks(ciphertext, bPlaintext)
	return hex.EncodeToString(ciphertext)
}

*/

var prefix []byte
var target []byte

func decryptPrefixBased(ciphertext, bKey, bIV, prefix []byte) bool {
	/*
		We decrypt the first block only and check if the prefix matches with "ractf"
	*/

	cipher, err := aes.NewCipher(bKey)

	if err != nil || len(ciphertext) != 16 {
		log.Println(err)
		return false
	}

	plaintext := make([]byte, 16)
	cipher.Decrypt(plaintext, ciphertext)

	// XOR to emulate ECB
	for i, b := range plaintext {
		plaintext[i] = bIV[i] ^ b
	}

	return bytes.HasPrefix(plaintext, prefix)
}

func force(base int64) {

	var k int64 = 0

	for ; k < (1 << 12); k++ {

		rand.Seed(base + k)
		for i := 0; i < rand.Intn(32); i++ {
			rand.Seed(rand.Int63())
		}

		var key []byte
		var iv []byte

		for i := 0; i < 32; i++ {
			key = append(key, byte(rand.Intn(255)))
		}

		for i := 0; i < aes.BlockSize; i++ {
			iv = append(iv, byte(rand.Intn(255)))
		}

		if decryptPrefixBased(target[:16], key, iv, prefix) {
			aesBC, _ := aes.NewCipher(key)
			plaintext := make([]byte, len(target))

			mode := cipher.NewCBCDecrypter(aesBC, iv)
			mode.CryptBlocks(plaintext, target)
			fmt.Println("Flag: ", string(plaintext))
		}
	}

	fmt.Println("Done with base", base)
}

/*
nums = (x for x in range(0,2**12 -1)) + (16777216 + x for x in range(0,2**12 -1))

000000000000000000000000000000000000001000000000000111111111111

2^12 combinations for the end part with

16777216 = 2^

*/

func main() {
	prefix = []byte("ractf") // unlikely that we have a match: 1/(2^{5*8})
	target, _ = hex.DecodeString("5e832b49ea133d275cc7c445372e0bb3394a1b371a1b377c967daf6d3d96afc1")

	bases := [2]int64{0, 1 << 24}

	fmt.Printf("Bruteforcing")

	for _, base := range bases {
		go force(base)
	}

	fmt.Scanln()

	//iv := hex.DecodeString("8cde1ac1b0862190213ecdb3351aa73f")
	//key := hex.DecodeString("f3e90b5ff8082c343ff5a64826977059b0cda07b1af1edfcee037228f5b822e3")
}
