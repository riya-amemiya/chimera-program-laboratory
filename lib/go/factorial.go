package main

import "fmt"
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}
func main() {
        for i := 0; i < 1000000; i++ {
				fmt.Printf("%d\n", factorial(10))
        }
}