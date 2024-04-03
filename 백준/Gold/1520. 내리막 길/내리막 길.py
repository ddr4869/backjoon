import sys
input = sys.stdin.readline
m,n=list(map(int, input().split()))
board=['' for i in range(m)]
for i in range(m):
    board[i]=list(map(int,input().split()))

cnt=0
dy,dx=[1,-1,0,0],[0,0,1,-1]

def dfs(y,x,dp,height):
    if y==m-1 and x==n-1: return 1 
    if dp[y][x]!=-1: return dp[y][x]
    cnt=0
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if 0<=ny<m and 0<=nx<n and board[ny][nx]<height:
            cnt+=dfs(ny,nx,dp,board[ny][nx])
    dp[y][x]=cnt
    return dp[y][x]

dp=[[-1 for _ in range(n)] for _ in range(m)]
dfs(0,0,dp,board[0][0])
print(dp[0][0])