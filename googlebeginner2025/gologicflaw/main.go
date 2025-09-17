package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func generateRandomNumberFromSeed(seed int64) int {
	rand.Seed(seed)
	return rand.Intn(1000000000)
}

func generateRandomNumber() int {
	rand.Seed(time.Now().UTC().Unix())
	return rand.Intn(1000000000)
}

func log(s string) {
	fmt.Println(fmt.Sprintf("[%d] %s", time.Now().UTC().Unix(), s))
}

func guessANumber(count int) bool {
	randNumber := generateRandomNumber()

	log(fmt.Sprintf("number %d: ", count))
	reader := bufio.NewReader(os.Stdin)
	line, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	number, err := strconv.Atoi(strings.TrimSpace(line))
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	if number == randNumber {
		return true
	}

	log(fmt.Sprintf("Guess failed: %d != %d", number, randNumber))
	return false
}

func win() {
	content, err := os.ReadFile("/flag")
	if err != nil {
		log("Unable to read the flag.")
		return
	}
	log(fmt.Sprintf("Here is your flag: %s", string(content)))
}

func main() {
	if len(os.Args) == 2 {
		arg_seed := os.Args[1]
		seed, _ := strconv.Atoi(arg_seed)
		println(generateRandomNumberFromSeed(int64(seed)))
	} else {
		log("Guess three random numbers and win the flag!")
		for i := 1; i <= 3; i++ {
			success := guessANumber(i)
			if !success {
				log("No flag for you. bye bye ..")
				return
			}
		}
		win()
	}
}
