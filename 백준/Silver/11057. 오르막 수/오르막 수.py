import sys
n = int(input())
dp = [[0 for _ in range(10)]] * (n+1)
for i in range(10):
    dp[1][i] = 1
k=2
while(k <= n):
    for i in range(10):
        total = 0
        for j in range(i, 10):
            total += (dp[k-1][j]%10007)
        dp[k][i] = total
    k += 1
print(sum(dp[n])%10007)