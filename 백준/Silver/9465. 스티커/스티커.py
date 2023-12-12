import sys
input = sys.stdin.readline

t = int(input())

while(t):
    n = int(input())
    stickers = [[0 for j in range(n)] for i in range(2)]

    stickers_input=list(map(int, input().split()))
    stickers[0]=stickers_input
    stickers_input=list(map(int, input().split()))
    stickers[1]=stickers_input

    if n==1:
        print(max(stickers[0][0], stickers[1][0]))
        t-=1
        continue

    dp = [[0 for j in range(n)] for i in range(2)]
    dp[0][0]=stickers[0][0]
    dp[1][0]=stickers[1][0]
    dp[0][1]=stickers[1][0]+stickers[0][1]
    dp[1][1]=stickers[0][0]+stickers[1][1]
    bigest=[]
    bigest.append(max(dp[0][0], dp[1][0]))
    bigest.append(max(dp[0][1], dp[1][1]))

    for i in range(2,n):
        # dp[i-2]+max(stickers[0][i],stickers[1][i])
        # dp[i-1]
        dp[0][i]=max(dp[1][i-1], bigest[i-2])+stickers[0][i]
        dp[1][i]=max(dp[0][i-1], bigest[i-2])+stickers[1][i]
        bigest.append(max(dp[0][i],dp[1][i]))

    print(bigest[-1])
    t-=1