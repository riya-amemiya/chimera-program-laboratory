package main

import "C"

//export golang_factorial
func golang_factorial(n int) int {
        if n == 0 {
                return 1
        }
        return n * golang_factorial(n-1)
}

func main() {
}