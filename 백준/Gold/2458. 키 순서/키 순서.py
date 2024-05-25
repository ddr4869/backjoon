import sys
input = sys.stdin.readline
n, m = map(int, input().split())
heights=[[0 for _ in range(n+1)] for _ in range(n+1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    heights[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if heights[i][k]==1 and heights[k][j]==1:
                heights[i][j]=1

for i in range(1,n+1):
    cnt=0
    for j in range(1,n+1):
        cnt += heights[i][j]+heights[j][i]
    if cnt == n-1: 
        answer += 1

print(answer)