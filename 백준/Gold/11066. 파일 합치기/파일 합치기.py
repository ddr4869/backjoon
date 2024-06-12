import sys
from collections import defaultdict
link = defaultdict(int)
t = int(input())
while(t):
    t -= 1
    n = int(input())
    files = [0] + list(map(int, input().split()))
    total = 0
    accumulate = []
    for file in files:
        total += file
        accumulate.append(total)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        if 0 <= i-1:
            dp[i][i-1] = (files[i] + files[i-1])
        if i+1 <= n:
            dp[i][i+1] = (files[i] + files[i+1])
    
    for length in range(2, n + 1):  
        for i in range(1, n - length + 2): 
            j = i + length - 1  
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + accumulate[j] - accumulate[i - 1])

    print(dp[1][n])