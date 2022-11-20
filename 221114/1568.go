package main

import (
	"bufio"
	"fmt"
	"os"
)

var cnt int

func main() {
	r := bufio.NewReader(os.Stdin)
	var N, K int
	fmt.Fscan(r, &N)
	cnt = 0
	K = 1
	solve(N, K)
	fmt.Println(cnt)
}

func solve(n, k int) {
	if n == k {
		cnt++
		return
	} else if n < k {
		solve(n, 1)
	} else {
		cnt++
		solve(n-k, k+1)
	}
	return
}
