import sys
input = sys.stdin.readline
n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
HEIGHT=sum(cost)+1
if HEIGHT==0:
    print(0); sys.exit(0)
dp = [[0 for _ in range(n)] for _ in range(HEIGHT)]
for i in range(cost[0], HEIGHT):
    dp[i][0] = memory[0]
for i in range(HEIGHT):
    for j in range(1, n):
        if i-cost[j] >= 0:
            dp[i][j] = max(dp[i][j-1], dp[i-cost[j]][j-1] + memory[j])
        else:
            dp[i][j] = dp[i][j-1]

for i,d in enumerate(dp):
    if max(d)>=m:
        print(i)
        break