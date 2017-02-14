//Acesse meu [post](http://romulojales.com/golang-e-testes/) sobre os arquivos e testes desta pasta
package main

import "testing"


func BenchmarkMultiplicaSomando(b *testing.B) {
	for i := 0; i < b.N; i++ {
		multiplicaSomando(-4, -3)
		multiplicaSomando(-4, -1)

		multiplicaSomando(4, -3)
		multiplicaSomando(4, -1)
		multiplicaSomando(4, 0)

		multiplicaSomando(4, 1)
		multiplicaSomando(4, 5)
	}
}

func BenchmarkMultiplica(b *testing.B) {
	for i := 0; i < b.N; i++ {
		multiplica(-4, -3)
		multiplica(-4, -1)

		multiplica(4, -3)
		multiplica(4, -1)
		multiplica(4, 0)

		multiplica(4, 1)
		multiplica(4, 5)
	}
}