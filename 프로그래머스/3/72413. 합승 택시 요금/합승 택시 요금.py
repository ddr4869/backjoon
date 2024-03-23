from collections import defaultdict, deque
def solution(n, s, a, b, fares):
    dp=[[10e10 for _ in range(n+1)] for _ in range(n+1)]

    for start,arrive,cost in fares:
        dp[start][arrive]=cost
        dp[arrive][start]=cost
    
    for i in range(n+1):
        dp[i][i]=0

    ans=[]
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][j]>dp[i][k]+dp[k][j]:
                    dp[i][j]=dp[i][k]+dp[k][j]
    
    answer=10e10

    for i in range(1,n+1):
        StoI=dp[s][i]
        ItoA=dp[i][a]
        ItoB=dp[i][b]
        answer=min(answer, StoI+ItoA+ItoB)
    return answer