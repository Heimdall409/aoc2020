package dayXX

import (
	"os"
	"strings"
	"testing"

	R "github.com/stretchr/testify/require"
)

const (
	inputFile   = "./input.txt"
	exampleFile = "./example.txt"
)

// ReadInput retrieves the content of the input file
func ReadInput(filepath string) []string {
	data, _ := os.ReadFile(filepath)
	return strings.Split(string(data), "\n")
}

func First(input []string) interface{} {
	return nil
}

func Second(input []string) interface{} {
	return nil
}

func TestDay(t *testing.T) {
	r := R.New(t)
	example := ReadInput(exampleFile)
	input := ReadInput(inputFile)
	r.Equal(nil, First(example))
	r.Equal(nil, First(input))
	r.Equal(nil, Second(example))
	r.Equal(nil, Second(input))
}
