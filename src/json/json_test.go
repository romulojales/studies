package main
import (
	"testing"
	"encoding/json"
	"bytes"
	"fmt"
)


type Nosj struct {
	Sort []string
}

func TestJson(t *testing.T) {
	b := Nosj{[]string{"issued", "fake"}}
		fmt.Println("%v", b)

	jsonb, _ := json.Marshal(b)
	ctrl := []byte(`{"Sort":["issued", "fake"]}`)
	fmt.Println(jsonb)
	fmt.Println(ctrl)
	if !bytes.Equal(jsonb, ctrl) {
		t.Error("Json errado: %q", jsonb)
	}
}
