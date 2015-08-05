package main
import (
	"testing"
	"encoding/json"
	"bytes"
	"fmt"
)

type QueryEsearch struct {
	Sort   interface{} `json:"sort"`
	Fields []string `json:"fields"`
}

func TestJson(t *testing.T) {
	arr := QueryEsearch{Sort: []string{"issued", "fake"}, Fields: []string{"123", "321"}}
	jsonb, _ := json.Marshal(arr)

	ctrl := []byte(`{"sort":["issued","fake"],"fields":["123","321"]}`)
	fmt.Println(string(jsonb))
	fmt.Println(string(ctrl))
	if !bytes.Equal(jsonb, ctrl) {
		t.Error("Json errado: %q", jsonb)
	}
}
