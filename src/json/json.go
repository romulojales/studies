package main

type SimpleJson struct {
	Sort   interface{} `json:"sort"`
	Fields []string `json:"fields"`
	Const  string `json:"const"`
}

type ComplexJson struct {
	Complex []SimpleJson `json:"complex"`
}