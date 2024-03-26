from collections import deque
def solution(m, n, puddles):
    if m==1 or n==1:
        if len(puddles[0])==0: return 1
        return 0
    maps=[[0 for _ in range(m)] for _ in range(n)]
    for x,y in puddles:
        maps[y-1][x-1]=-1

    for i in range(n):
        if maps[i][0]!=-1:
            maps[i][0]=1
        else: break
    for j in range(m):
        if maps[0][j]!=-1:
            maps[0][j]=1
        else: break
    for i in range(1,n):
        for j in range(m):
            if maps[i][j]==-1: continue
            if maps[i][j]!=-1:
                left=maps[i][j-1] if maps[i][j-1]!=-1 else 0
                upper=maps[i-1][j] if maps[i-1][j]!=-1 else 0
                maps[i][j]=(left+upper)%1000000007
    return maps[n-1][m-1]