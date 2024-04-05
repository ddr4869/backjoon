import sys
from collections import defaultdict
input = sys.stdin.readline
n,m,h=list(map(int, input().split()))
board=[[0 for _ in range(n)] for _ in range(h)]
for i in range(m):
    a,b=list(map(int, input().split()))
    a-=1; b-=1
    board[a][b]=1


def check_answer():
    for start in range(n): 
        now = start 
        for j in range(h): 
            if board[j][now]: 
                now += 1 
            elif now > 0 and board[j][now - 1]: 
                now -= 1 
        if now != start: 
          return False  
    return True


def dfs(y,x,ans):
    global answer
    if ans>3 or ans>=answer: return 
    if check_answer(): 
        if answer>ans: answer=ans
        return
    for i in range(y,h):
        for j in range(0,n-1):
            if (i==y and j<x) or board[i][j]: continue
            if j>=1 and board[i][j-1]: continue
            if j<=n-2 and board[i][j+1]: continue
            board[i][j]=1
            dfs(i,j,ans+1)
            board[i][j]=0

answer=4
dfs(0,0,0)
if answer==4: answer=-1
print(answer)