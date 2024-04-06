import sys
from collections import defaultdict, deque
from itertools import combinations
input = sys.stdin.readline
n,m=list(map(int, input().split()))
board=[]
virus=[]; virus_cnt=0; zero_cnt=0
answer=1000000
for i in range(n):
    board.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            virus.append((i,j,virus_cnt))
            virus_cnt+=1
        if board[i][j]==0: zero_cnt+=1

dy,dx=[1,-1,0,0],[0,0,1,-1]

for comb in list(combinations(range(virus_cnt), m)):
    q=deque()
    this_board=[row[:] for row in board]
    visited=[[False for _ in range(n)] for _ in range(n)]
    zero=0
    for i in comb:
        q.append((virus[i][0],virus[i][1], 0))
        visited[virus[i][0]][virus[i][1]]=True
    while(q):
        y,x,time=q.popleft()
        if zero==zero_cnt: break
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and this_board[ny][nx]!=1:
                if this_board[ny][nx]==0: zero+=1
                visited[ny][nx]=True
                this_board[ny][nx]=-1
                q.append((ny,nx,time+1))
    if zero==zero_cnt:
        if q: time=q[-1][2]
        answer=min(answer,time)

print(answer if answer!=1000000 else -1)