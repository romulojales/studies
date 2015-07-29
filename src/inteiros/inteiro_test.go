package main

import "testing"

func TestSomaUmMaisDois(t *testing.T){
	x := soma(1, 2)
	if x != 3 {
	 t.Error("Opa! 1 + 2 não é igual a 3, obtive", x)
	}
}

func TestSomaUmMaisUm(t *testing.T){
	x := soma(1, 1)
	if x != 2 {
	 t.Error("Opa! 1 + 1 não é igual a 2, obtive", x)
	}
}

func TestDivide(t *testing.T){
	x, err := divide(4, 2)
	if err != nil{
		 t.Error("não era esperado o erro", err)
	}	
	if x != 2 {
	 t.Error("Opa! 4 / 2 não é igual a 2, obtive", x)
	}
}

func TestDivideSemErro(t *testing.T){
	_, err := divide(4, 2)
	if err != nil{
		t.Error("não era esperado o erro", err)
	}	
}

func TestDividePorZero(t *testing.T){
	_, err := divide(4, 0)
	if err != errorDivisorZero {
	 t.Error(err)
	}
}


func TestSubtrai(t *testing.T){
	resultado := subtrai(4, 5)
	if resultado != -1 {
	 t.Error("curioso, na terra dos gophers 4-5 não é -1. é", resultado)
	}
}

