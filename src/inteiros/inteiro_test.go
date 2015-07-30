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

func TestMultiplicaSomandoSimples(t *testing.T){
	resultado := multiplicaSomando(4, 5)
	if resultado != 20 {
	 t.Errorf("4 * 5 não é 20 é %d", resultado)
	}
}

func TestMultiplicaSomandoPor0(t *testing.T){
	resultado := multiplicaSomando(4, 0)
	if resultado != 0 {
	 t.Errorf("4 * 0 não é 0 é %d", resultado)
	}
}

func TestMultiplicaSomandoPorMenos1(t *testing.T){
	resultado := multiplicaSomando(4, -1)
	if resultado != -4 {
	 t.Errorf("4 * -1 não é -4 é %d", resultado)
	}
}

func TestMultiplicaSomandoPor1(t *testing.T){
	resultado := multiplicaSomando(4, 1)
	if resultado != 4 {
	 t.Errorf("4 * 1 não é 4 é %d", resultado)
	}
}

func TestMultiplicaSomandoPorMenos3(t *testing.T){
	resultado := multiplicaSomando(4, -3)
	if resultado != -12 {
	 t.Errorf("4 * -3 não é -12 é %d", resultado)
	}
}

func TestMultiplicaSomandoMenosComMenos(t *testing.T){
	resultado := multiplicaSomando(-4, -3)
	if resultado != 12 {
	 t.Errorf("-4 * -3 não é 12 é %d", resultado)
	}
}


func TestMultiplicaSomandoMenosComMenosUm(t *testing.T){
	resultado := multiplicaSomando(-4, -1)
	if resultado != 4 {
	 t.Errorf("-4 * -1 não é 4 é %d", resultado)
	}
}



func TestMultiplicaSimples(t *testing.T){
	resultado := multiplica(4, 5)
	if resultado != 20 {
	 t.Errorf("4 * 5 não é 20 é %d", resultado)
	}
}

func TestMultiplicaPor0(t *testing.T){
	resultado := multiplica(4, 0)
	if resultado != 0 {
	 t.Errorf("4 * 0 não é 0 é %d", resultado)
	}
}

func TestMultiplicaPorMenos1(t *testing.T){
	resultado := multiplica(4, -1)
	if resultado != -4 {
	 t.Errorf("4 * -1 não é -4 é %d", resultado)
	}
}

func TestMultiplicaPor1(t *testing.T){
	resultado := multiplica(4, 1)
	if resultado != 4 {
	 t.Errorf("4 * 1 não é 4 é %d", resultado)
	}
}

func TestMultiplicaPorMenos3(t *testing.T){
	resultado := multiplica(4, -3)
	if resultado != -12 {
	 t.Errorf("4 * -3 não é -12 é %d", resultado)
	}
}

func TestMultiplicaMenosComMenos(t *testing.T){
	resultado := multiplica(-4, -3)
	if resultado != 12 {
	 t.Errorf("-4 * -3 não é 12 é %d", resultado)
	}
}

func TestMultiplicaMenosComMenosUm(t *testing.T){
	resultado := multiplica(-4, -1)
	if resultado != 4 {
	 t.Errorf("-4 * -1 não é 4 é %d", resultado)
	}
}

