from collections import deque 
def solution(board):
    y_length, x_length = len(board), len(board[0])
    visited=[[False for _ in range(x_length)] for _ in range(y_length)]
    start, target = (0,0),(0,0)
    for y in range(y_length):
        for x in range(x_length):  
            if board[y][x]=='R': start=(y,x); visited[y][x]=True
            if board[y][x]=='G': target=(y,x)
    dq=deque(); dq.append((start[0],start[1],0))
    locate=start
    def move(locate, direction):
        y,x,ans=locate 
        if direction==0: # left
            while(x-1>=0 and board[y][x-1]!='D'): x-=1
        if direction==1: # right
            while(x+1<x_length and board[y][x+1]!='D'): x+=1
        if direction==2: # down
            while(y-1>=0 and board[y-1][x]!='D'): y-=1
        if direction==3: # up
            while(y+1<y_length and board[y+1][x]!='D'): y+=1
        if (y,x)==(locate[0],locate[1]) or visited[y][x]: 
            return (-1,-1,-1)
        visited[y][x]=True
        return (y,x,ans+1) 
    
    while(dq):
        locate=dq.popleft()
        for direction in range(4):
            _next=move(locate, direction)
            if _next != (-1,-1,-1): 
                if (_next[0],_next[1])==target: 
                    return _next[2]
                dq.append(_next)
    return -1
