import sys
input = sys.stdin.readline
c, n = map(int, input().split())
costs = []
for i in range(n):
    cost,custom = map(int, input().split())
    costs.append((cost,custom))


dp=[1e9]*(c+1)
first=1e9

for i in range(0,n):
    if costs[i][1]<=c:
        dp[costs[i][1]]=min(dp[costs[i][1]], costs[i][0])
    else:
        first=min(first,costs[i][0])

for i in range(c+1):
    if dp[i]==1e9:
        continue
    for j in range(n):
        if i+costs[j][1]>=c:
            dp[-1]=min(dp[-1],dp[i]+costs[j][0])
            continue
        dp[i+costs[j][1]]=min(dp[i+costs[j][1]], dp[i]+costs[j][0])

print(min(dp[-1], first))

