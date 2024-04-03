import sys
from collections import defaultdict
input = sys.stdin.readline
r,c=list(map(int, input().split()))
board=['' for i in range(r)]
for i in range(r):
    board[i]=str(input().strip())

dy,dx=[1,-1,0,0],[0,0,1,-1]
answer=0
def dfs(board, alphabat, y, x, cnt):
    global answer
    if cnt>answer: answer=cnt
    ans=0
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if 0<=ny<r and 0<=nx<c and alphabat[ord(board[ny][nx])-65]==0:
            alphabat[ord(board[ny][nx])-65]=1
            ans=max(ans,dfs(board,alphabat,ny,nx,cnt+1))
            alphabat[ord(board[ny][nx])-65]=0
    return ans

alphabat=[0 for _ in range(26)]
alphabat[ord(board[0][0])-65]=1
dfs(board,alphabat,0,0,1)
print(answer)