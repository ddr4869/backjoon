import sys
n,m = list(map(int, input().split()))
board=[[] for _ in range(n)]
for i in range(n):
    board[i]=list(map(int, input().split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][j]>board[i][k]+board[k][j]:
                board[i][j]=board[i][k]+board[k][j]

while(m):
    a,b,c=list(map(int, input().split()))
    if board[a-1][b-1]<=c: print("Enjoy other party")
    else: print("Stay here")
    m-=1