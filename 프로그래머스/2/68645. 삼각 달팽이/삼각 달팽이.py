def solution(n):
    answer = []
    snail=[[0 for _ in range(n)] for _ in range(n)]
    cnt=2
    direction=0
    y,x,ny,nx=0,0,0,0
    endpoint=0
    
    snail[0][0]=1
    while(endpoint<=3):
        if (direction%3==0): ny,nx=y+1,x
        elif (direction%3==1): ny,nx=y,x+1
        elif (direction%3==2): ny,nx=y-1,x-1
        if 0<=ny<n and 0<=nx<n and snail[ny][nx]==0:
            snail[ny][nx]=cnt
            y,x=ny,nx
            cnt+=1
            endpoint=0
        else:
            direction+=1
            endpoint+=1
            
    for i in range(n):
        for j in range(0,i+1):
            answer.append(snail[i][j])

    return answer