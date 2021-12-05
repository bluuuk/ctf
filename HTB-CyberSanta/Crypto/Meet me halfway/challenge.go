package main

import (
	"crypto/aes"
	"encoding/hex"
	"fmt"
	"strings"
	"sync"

	"github.com/ernestosuarez/itertools"
)

func main() {

	map_encrypt := make(map[string]string)
	plaintext, _ := hex.DecodeString("3030303030303030303030303030303030303030303030303030303030303030")

	map_decrypt := make(map[string]string)
	ciphertext, _ := hex.DecodeString("ccd972d05bca994ffd3e4b8d54ed77c9ccd972d05bca994ffd3e4b8d54ed77c986d073696cd4c29689aaebc29ac0084f")

	challenge, _ := hex.DecodeString("2e9e5bf227e474ae67605dab1f1e915edd251129ad07389ff7e001cc1ecee8295de440ce95bdf0f049e29801108e04accbd1d1d5895f6c45e08a2fc78172d7c6f2c0ab7eec18cf265b6c7f831cc4ef2f922de3f946ac43f7a4dad6b9a81fecce")

	// we just take the first block
	ciphertext = ciphertext[:16]
	plaintext = plaintext[:16]

	wg := sync.WaitGroup{}
	wg.Add(2)

	go func() {
		defer wg.Done()
		meet_decrypt(ciphertext, map_decrypt)
	}()

	go func() {
		defer wg.Done()
		meet_encrypt(plaintext, map_encrypt)
	}()

	wg.Wait()

	for cipher, key_enc := range map_encrypt {
		if key_dec, contains := map_decrypt[cipher]; contains {
			fmt.Printf("Key `%s` and key `%s` provide successfull meet in the middle\n", key_enc, key_dec)

			temp := make([]byte, len(challenge))
			cipher1, _ := aes.NewCipher([]byte(key_enc))
			cipher2, _ := aes.NewCipher([]byte(key_dec))
			bs := 16

			for processed := 0; processed < len(challenge); processed += bs {
				cipher2.Decrypt(temp[processed:processed+bs], challenge[processed:processed+bs])
				cipher1.Decrypt(temp[processed:processed+bs], temp[processed:processed+bs])
			}

			fmt.Println(strings.TrimSpace(string(temp)))
		}
	}

}

func meet_encrypt(plaintext []byte, out map[string]string) {
	index_list := make([]int, 16)
	for i, _ := range index_list {
		index_list[i] = i
	}

	alphabet := []byte("0123456789abcdef")

	key_part := []byte("cyb3rXm45!@#")
	key := make([]byte, 16)
	copy(key, key_part)

	for perm := range itertools.PermutationsInt(index_list, 4) {
		for index, val := range perm {
			key[index+12] = alphabet[val]
		}

		ciphertext := make([]byte, 16)

		cipher, _ := aes.NewCipher(key)
		cipher.Encrypt(ciphertext, plaintext)
		out[string(ciphertext)] = string(key)
	}
}

func meet_decrypt(ciphertext []byte, out map[string]string) {
	index_list := make([]int, 16)
	for i, _ := range index_list {
		index_list[i] = i
	}

	alphabet := []byte("0123456789abcdef")

	key_part := []byte("cyb3rXm45!@#")
	key := make([]byte, 16)
	copy(key[4:], key_part)

	for perm := range itertools.PermutationsInt(index_list, 4) {
		for index, val := range perm {
			key[index] = alphabet[val]
		}
		plaintext := make([]byte, 16)

		cipher, _ := aes.NewCipher(key)
		cipher.Decrypt(plaintext, ciphertext)
		out[string(plaintext)] = string(key)
	}
}
