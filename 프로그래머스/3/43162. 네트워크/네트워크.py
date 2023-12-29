from collections import deque
def solution(n, computers):
    answer = 0
    links=[]
    for i in range(n):
        link=deque()
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                link.append(j)
        links.append(link)
    remain=[True for _ in range(n)]
    
    for i in range(n):
        if not remain[i]:
            continue
        remain[i]=False
        this_deque=links[i]
        while(this_deque):
            next_idx=this_deque.popleft()
            if not remain[next_idx]:
                continue 
            while(links[next_idx]):
                this_deque.append(links[next_idx].popleft())
            remain[next_idx]=False
        answer+=1
              
    return answer