# 플로이드
def solution(N, road, K):
    dp=[[10e8 for _ in range(N+1)] for _ in range(N+1)]
    for start,arrive,cost in road:
        dp[start][arrive]=min(cost,dp[start][arrive])
        dp[arrive][start]=min(cost,dp[arrive][start])
    for i in range(1,N+1):
        dp[i][i]=0
    
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if dp[i][j]>dp[i][k]+dp[k][j]:
                    dp[i][j]=dp[i][k]+dp[k][j]
    answer=0
    for i in range(1,N+1):
        if dp[1][i]<=K: answer+=1
    return answer