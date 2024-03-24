def solution(n, results):
    answer = 0
    distance=[[100 for _ in range(n+1)] for _ in range(n+1)]
    for start, arrive in results:
        distance[start][arrive]=1
    for i in range(n+1):
        distance[i][i]=0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if distance[i][j]>distance[i][k]+distance[k][j]:
                    distance[i][j]=distance[i][k]+distance[k][j]
    
    for i in range(1,n+1):
        cnt=0
        for j in range(1,n+1):
            if distance[i][j]!=100 or distance[j][i]!=100:
                cnt+=1
        if cnt==n: answer+=1
    return answer
                
        
        
                