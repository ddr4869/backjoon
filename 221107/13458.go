package main

import (
	"bufio"
	"fmt"
	"os"
)

var A [1000010]int

func main() {
	r := bufio.NewReader(os.Stdin)
	var N, B, C int

	fmt.Fscan(r, &N)
	for i := 0; i < N; i++ {
		fmt.Fscan(r, &A[i])
	}
	fmt.Fscan(r, &B)
	fmt.Fscan(r, &C)
	solve(N, B, C)
}

func solve(n, b, c int) {
	//fmt.Printf("%d %d %d", n, b, c)
	cnt := n
	for i := 0; i < n; i++ {
		if A[i]-b <= 0 {
			continue
		}
		cnt += ((A[i]-b-1)/c + 1)
	}
	fmt.Println(cnt)
}
