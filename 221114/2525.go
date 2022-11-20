package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var hour, min, add_min int
	fmt.Fscan(r, &hour, &min, &add_min)

	add_min += min
	hour += add_min / 60
	min = add_min % 60
	if hour >= 24 {
		hour -= 24
	}
	fmt.Printf("%d %d", hour, min)
}
