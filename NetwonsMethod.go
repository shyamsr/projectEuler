// Netwtons Method to find Square root
// Approximation
package main

import (
	"fmt"
)

func Sqrt(x float64) (z float64) {
	z = float64(1)
	for i:=0;i<10;i++ {
		z = z - ((z*z - x) / (2*z))
	}
	return
}

func main() {
	fmt.Println(Sqrt(10))
}

