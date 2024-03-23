def solution(triangle):
    dp=[[-1 for _ in range(501)] for _ in range(501)]
    dp[0][0]=triangle[0][0]
    for y in range(1,len(triangle)):
        for x in range(0,y+1):
            dp[y][x]=max(dp[y-1][x-1],dp[y-1][x])+triangle[y][x] if x-1>=0 else dp[y-1][x]+triangle[y][x]
    return max(dp[len(triangle)-1])