import sys
from collections import defaultdict, deque
from itertools import combinations
input = sys.stdin.readline
n,m=list(map(int, input().split()))
board=[]
cctv=[]
answer=64
for i in range(n):
    board.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5: cctv.append((i,j,board[i][j]))

# 0->북 1->남 2->동 3->서
def mark_board(bo,y,x,direction):
    board = [row[:] for row in bo] 
    if direction==0: #북
        move=1
        while(y+move<n and board[y+move][x]!=6):
            if board[y+move][x]==0: board[y+move][x]=1
            move+=1
    elif direction==1: #남
        move=-1
        while(y+move>=0 and board[y+move][x]!=6):
            if board[y+move][x]==0: board[y+move][x]=1
            move-=1
    elif direction==2: #동
        move=1
        while(x+move<m and board[y][x+move]!=6):
            if board[y][x+move]==0: board[y][x+move]=1
            move+=1
    elif direction==3: #서
        move=-1
        while(x+move>=0 and board[y][x+move]!=6):
            if board[y][x+move]==0: board[y][x+move]=1
            move-=1
    return board

def dfs(board, idx):
    if idx==len(cctv):
        global answer
        hide=0
        for b in board:
            hide+=b.count(0)
        if hide<answer: answer=hide
        return
    if cctv[idx][2]==1:
        dfs(mark_board(board[:],cctv[idx][0],cctv[idx][1],0), idx+1)
        dfs(mark_board(board[:],cctv[idx][0],cctv[idx][1],1), idx+1)
        dfs(mark_board(board[:],cctv[idx][0],cctv[idx][1],2), idx+1)
        dfs(mark_board(board[:],cctv[idx][0],cctv[idx][1],3), idx+1)
    elif cctv[idx][2]==2:
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],0)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],1)
        dfs(this_board, idx+1)
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],2)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],3)
        dfs(this_board, idx+1)
    elif cctv[idx][2]==3:
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],0)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],2)
        dfs(this_board, idx+1)
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],2)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],1)
        dfs(this_board, idx+1)
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],1)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],3)
        dfs(this_board, idx+1)
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],3)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],0)
        dfs(this_board, idx+1)
    elif cctv[idx][2]==4:
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],0)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],1)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],2)
        dfs(this_board, idx+1)
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],0)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],1)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],3)
        dfs(this_board, idx+1)
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],0)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],2)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],3)
        dfs(this_board, idx+1)
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],1)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],2)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],3)
        dfs(this_board, idx+1)
    elif cctv[idx][2]==5:
        this_board=mark_board(board[:],cctv[idx][0],cctv[idx][1],0)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],1)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],2)
        this_board=mark_board(this_board[:],cctv[idx][0],cctv[idx][1],3)
        dfs(this_board, idx+1)

dfs(board,0)
print(answer)