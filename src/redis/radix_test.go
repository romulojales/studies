package redis
import (
	"testing"
)


func TestRedisSentinelPing(t *testing.T) {
	_, err := GetSetinelClient()
	if err != nil {
		t.Errorf("Erro no teste de conexão. %s", err.Error())
	}
}

func TestRedisPing(t *testing.T) {
	resp, err := PingSentinel()
	if err != nil {
		t.Errorf("Não deveria gerar erro. %s", err.Error())
	}

	if resp != "Resp(Str PONG)"{
		t.Errorf("ACE %s", resp)
	}
}
