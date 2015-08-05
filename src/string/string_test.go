package string
import "testing"


func TestStringComoArgumento(t *testing.T) {
	x := retonaString("abc1")
	if x != "abc1" {
		t.Errorf("Não retornou abc1")
	}
}
