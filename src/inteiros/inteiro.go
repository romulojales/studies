package main

import "errors"

var errorDivisorZero = errors.New("O divisor da operação não pode ser zero")


func soma(x, y int) int {
 return x + y
}

func divide(x, y int) (int, error){
 var err error
 var resultado int
 if y == 0{
   err = errorDivisorZero
 }else{
  resultado = x / y
 }
 return resultado, err
}

func subtrai(x, y int) int {
 return x - y
}

