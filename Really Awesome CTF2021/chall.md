> The goal of the challenge is to bruteforce a an aes key

The key is generated with a seed that depends on the current time. The mask `0x7FFFFFFFFEFFF000` allows us to reduce the bruteforce range
such that we only have to test $2^{13}$ possibilities for the seed.

```go
        curr := time.Now().UnixNano()
		seed := curr & ^0x7FFFFFFFFEFFF000
		fmt.Println("Time:", curr, "Seed:", seed)
		rand.Seed(seed)
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
``` 