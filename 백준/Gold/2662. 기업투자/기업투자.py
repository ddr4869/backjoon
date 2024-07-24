import sys
input = sys.stdin.readline

n, m = map(int, input().split())
profits = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(1, m + 1):
        profits[i][j] = data[j]

dp = [[0] * (n + 1) for _ in range(m + 1)]
invest = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(0, j + 1):
            current_profit = dp[i - 1][j - k] + profits[k][i]
            if current_profit > dp[i][j]:
                dp[i][j] = current_profit
                invest[i][j] = k

max_profit = dp[m][n]
print(max_profit)

result = [0] * m
remaining_money = n
for company in range(m, 0, -1):
    result[company - 1] = invest[company][remaining_money]
    remaining_money -= invest[company][remaining_money]

print(' '.join(map(str, result)))
