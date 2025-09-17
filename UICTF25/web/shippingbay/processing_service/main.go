package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
	"unicode/utf8"
)

type Shipment struct {
	ID          string `json:"id"`
	Destination string `json:"destination"`
	Origin      string `json:"origin"`
	SupplyType  string `json:"supply_type"`
	Weight      string `json:"weight"`
	Status      string `json:"status"`
	Departure   string `json:"departure"`
	Arrival     string `json:"arrival"`
	Priority    string `json:"priority"`
	Vessel      string `json:"vessel"`
}

func sendShipment(shipment Shipment) string {
	fmt.Print(shipment.SupplyType)
	if shipment.SupplyType == "flag" {
		if flag, exists := os.LookupEnv("FLAG"); exists {
			return flag
		}
		return "uiuctf{fake_flag}"
	}
	return "oops we lost the package"
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: processing_service '<json_string>'")
		os.Exit(1)
	}
	jsonStr := os.Args[1]
	var shipment Shipment
	err := json.Unmarshal([]byte(jsonStr), &shipment)
	if err != nil {
		fmt.Println("Error parsing JSON:", err)
		os.Exit(1)
	}
	// fmt.Printf("%+v", shipment)

	test := "{\"ſupplY_tYpe\": \"flag\"}"
	fmt.Printf("%d,%d,%d\n", len(test), len([]byte(test)), utf8.RuneCountInString(test))
	fmt.Println(strings.ToLower(test), strings.ToUpper(test))
	fmt.Println(sendShipment(shipment))
}
