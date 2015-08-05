package main
import (
	"testing"
	"encoding/json"
	"bytes"
)

type SimpleJson struct {
	Sort   interface{} `json:"sort"`
	Fields []string `json:"fields"`
	Const  string `json:"const"`
}

type ComplexStruct struct {
	Complex []SimpleJson `json:"complex"`
}


func TestMarshalSimpleJson(t *testing.T) {
	arr := SimpleJson{Sort: []string{"issued", "fake"}, Fields: []string{"123", "321"}}
	jsonb, _ := json.Marshal(arr)

	ctrl := []byte(`{"sort":["issued","fake"],"fields":["123","321"],"const":""}`)

	if !bytes.Equal(jsonb, ctrl) {
		t.Error("Jsonb errado: %q", string(jsonb))
		t.Error("ctrl errado: %q", string(ctrl))
	}
}

func TestMarshalComplexJson(t *testing.T) {
	ctrl := []byte(`{"complex":[{"sort":["issued","fake"],"fields":["123","321"],"const":"abc"}]}`)
	arr := ComplexStruct{Complex:[]SimpleJson{SimpleJson{Sort: []string{"issued", "fake"}, Fields:
	[]string{"123", "321"}, Const: "abc"}}}
	jsonb, _ := json.Marshal(arr)

	if !bytes.Equal(jsonb, ctrl) {
		t.Error("Jsonb errado", string(jsonb))
		t.Error("ctrl errado", string(ctrl))
	}

}


func TestUnMarshalComplexJson(t *testing.T) {
	ctrl := []byte(`{"complex":[{"sort":["issued","fake"],"fields":["123","321"],"const":"abc"}]}`)
	arr := ComplexStruct{}
	json.Unmarshal(ctrl, &arr)

	if arr.Complex[0].Fields[0] != "123"{
		t.Error("Jsonb errado", string(arr.Complex[0].Fields[0]))
	}

}