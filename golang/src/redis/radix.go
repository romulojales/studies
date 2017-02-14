package redis


import "github.com/mediocregopher/radix.v2/sentinel"


func GetSetinelClient() (*sentinel.Client, error) {
	client, err := sentinel.NewClient("tcp", "localhost:26379", 100, "mymaster")
	return client, err
}

func PingSentinel() (string, error){
	client, err := GetSetinelClient()
	if err != nil{
		return "", err
	}
	c, err := client.GetMaster("mymaster")
	if err != nil{
		return "", err
	}
	resp := c.Cmd("Ping").String()
	return resp, err
}

