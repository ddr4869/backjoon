from collections import deque

def solution(maps):
    sy,sx,ly,lx,ey,ex=0,0,0,0,0,0
    dy,dx=[1,-1,0,0],[0,0,1,-1]
    lever,exit=0,0
    height,width=len(maps),len(maps[0])
    visited=[[False for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if maps[y][x]=='S': sy=y; sx=x
            if maps[y][x]=='L': ly=y; lx=x
            if maps[y][x]=='E': ey=y; ex=x

    dq=deque()
    dq.append((sy,sx,0))
    visited[sy][sx]=True
    while(dq):
        y,x,ans=dq.popleft()
        if y==ly and x==lx: lever=ans; break
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<height and 0<=nx<width and maps[ny][nx]!='X' and visited[ny][nx]==False:
                dq.append((ny,nx,ans+1))
                visited[ny][nx]=True
    
    dq=deque()
    dq.append((ly,lx,0))
    visited=[[False for _ in range(width)] for _ in range(height)]
    visited[ly][lx]=True
    while(dq):
        y,x,ans=dq.popleft()
        if y==ey and x==ex: exit=ans
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<height and 0<=nx<width and maps[ny][nx]!='X' and visited[ny][nx]==False:
                dq.append((ny,nx,ans+1))
                visited[ny][nx]=True
    return -1 if (lever==0 or exit==0) else lever+exit