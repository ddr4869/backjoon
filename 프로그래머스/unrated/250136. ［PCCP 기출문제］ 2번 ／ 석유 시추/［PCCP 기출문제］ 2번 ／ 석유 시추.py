from collections import deque
def solution(land):
    answer = 0
    n=len(land)
    m=len(land[0])
    flag=[[False for _ in range(m)] for _ in range(n)]
    answers=[0 for _ in range(m)]
    
    for y in range(n):
        for x in range(m):
            if land[y][x] and not flag[y][x]:
                dq=deque()
                dq.append((y,x))
                flag[y][x]=True
                left,right=x,x
                cnt=1
                while(dq):
                    ny,nx=dq.popleft()
                    if ny+1<n and land[ny+1][nx] and not flag[ny+1][nx]: 
                        dq.append((ny+1,nx))
                        flag[ny+1][nx]=True
                        cnt+=1
                    if ny-1>=0 and land[ny-1][nx] and not flag[ny-1][nx]: 
                        dq.append((ny-1,nx))
                        flag[ny-1][nx]=True
                        cnt+=1
                    if nx+1<m and land[ny][nx+1] and not flag[ny][nx+1]:
                        dq.append((ny,nx+1))
                        flag[ny][nx+1]=True
                        if nx+1>right: right=nx+1
                        cnt+=1
                    if nx-1>=0 and land[ny][nx-1] and not flag[ny][nx-1]:
                        dq.append((ny,nx-1))
                        flag[ny][nx-1]=True
                        if nx-1<left: left=nx-1
                        cnt+=1
                for i in range(left,right+1):
                    answers[i]+=cnt      

    for ans in answers:
        answer=max(answer,ans)
    return answer
