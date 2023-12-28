from collections import deque
def solution(maps):
    dq=deque()
    dq.append((0,0,1))
    N=len(maps)
    M=len(maps[0])
    dp=[[0 for _ in range(M)] for _ in range(N)]
    while dq:
        v=dq.popleft()
        if dp[v[0]][v[1]]==0:
            dp[v[0]][v[1]]=v[2]
        else:
            continue
        if v[0]+1<N and maps[v[0]+1][v[1]]:
            dq.append((v[0]+1,v[1],v[2]+1))
        if v[0]-1>=0 and maps[v[0]-1][v[1]]:
            dq.append((v[0]-1,v[1],v[2]+1))
        if v[1]+1<M and maps[v[0]][v[1]+1]:
            dq.append((v[0],v[1]+1,v[2]+1))
        if v[1]-1>=0 and maps[v[0]][v[1]-1]:
            dq.append((v[0],v[1]-1,v[2]+1))

    return -1 if dp[N-1][M-1]==0 else dp[N-1][M-1] 