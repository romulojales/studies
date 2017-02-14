//Acesse meu [post](http://romulojales.com/golang-e-testes/) sobre os arquivos e testes desta pasta
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

	func multiplicaSomando(x, y int) int{
		resultado := 0
		if y > 0{
		 for i := 0; i<y; i++{
			resultado = soma(resultado, x)
		 }
		}else if y < 0{
			for i := y; i<0; i++ {
				resultado = subtrai(resultado, x)
			}
		}

		return resultado;
	}

func multiplica(x, y int) int{

	return x * y;
}