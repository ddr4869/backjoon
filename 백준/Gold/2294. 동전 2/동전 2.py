n, k = map(int, input().split()) 
coins = [int(input()) for i in range(n)]
dp = [ [0 for i in range(2)] for i in range(k+1)]

for i in range(k+1):
    dp[i][1]=100010

dp[0][0]=1
dp[0][1]=0

for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j][0] += dp[j-i][0]
            dp[j][1] = min(dp[j][1], dp[j-i][1]+1)

if dp[k][1]==100010:
    print(-1)
else:
    print(dp[k][1])