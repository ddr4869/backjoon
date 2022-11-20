package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var x, y int

	fmt.Fscan(r, &x, &y)
	if x > 0 && y > 0 {
		fmt.Println("1")
	} else if x < 0 && y > 0 {
		fmt.Println("2")
	} else if x > 0 && y < 0 {
		fmt.Println("4")
	} else if x < 0 && y < 0 {
		fmt.Println("3")
	}
}
