from collections import deque
def solution(board):
    answer = []
    N,M=len(board),len(board[0])
    visited=[[[10e6, 10e6] for _ in range(M)] for _ in range(N)]
    dq=deque()
    if board[0][1]!=1:
        dq.append((0,1,'x',100)); visited[0][1][0]=100
    if board[1][0]!=1:
        dq.append((1,0,'y',100)); visited[1][0][1]=100 #(y,x,direction,cost)
        
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    
    while(dq):
        y,x,direction,cost=dq.popleft()
        if y==N-1 and x==M-1: 
            answer.append(cost)
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<N and 0<=nx<M and board[ny][nx]!=1:
                if direction=='x' and dx[i]==0 and cost+600<visited[ny][nx][1]: # y로 전환
                    visited[ny][nx][1]=cost+600
                    dq.append((ny,nx,'y',cost+600))
                elif direction=='x' and dx[i]!=0 and cost+100<visited[ny][nx][0]:
                    visited[ny][nx][0]=cost+100
                    dq.append((ny,nx,'x',cost+100))
                elif direction=='y' and dy[i]==0 and cost+600<visited[ny][nx][0]: # x로 전환
                    visited[ny][nx][0]=cost+600
                    dq.append((ny,nx,'x',cost+600))
                elif direction=='y' and dy[i]!=0 and cost+100<visited[ny][nx][1]:
                    visited[ny][nx][1]=cost+100
                    dq.append((ny,nx,'y',cost+100))
    answer.sort()
    return answer[0]