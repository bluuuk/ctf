package main

import (
	"encoding/json"
	"strings"
	"testing"
	"unicode"
	"unicode/utf8"
)

func FuzzMain(f *testing.F) {
	orig := "supply_type"
	f.Add(orig)
	f.Fuzz(func(t *testing.T, jsonStr string) {
		if strings.ToLower(jsonStr) == orig {
			t.Skip()
		}

		assembled_json := "{\"" + jsonStr + "\":\"flag\"}"
		var shipment Shipment
		err := json.Unmarshal([]byte(assembled_json), &shipment)
		if err != nil {
			t.Skip()
		}

		if shipment.SupplyType == "flag" {
			for _, c := range assembled_json {
				if c > unicode.MaxASCII {
					t.Errorf("%s(%d-%d) caused a right flag: %v(%d)", jsonStr, utf8.RuneCountInString(jsonStr), utf8.RuneCountInString(orig), []byte(jsonStr), len([]byte(jsonStr)))
					break
				}
			}
		}
	})
}
