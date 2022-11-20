package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)
	solve(n)
}

func solve(n int) {
	var cnt int
	if n >= 100 {
		var a, b, c int
		cnt = 99
		for i := 100; i <= n; i++ {
			a = i / 100
			b = (i % 100) / 10
			c = i % 10
			if (a == b) && (b == c) {
				cnt++
			} else if (a - b) == (b - c) {
				cnt++
			}
		}
	} else {
		cnt = n
	}
	fmt.Println(cnt)
}
