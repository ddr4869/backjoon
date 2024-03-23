from collections import defaultdict, deque
def solution(n, edges):
    visited=[0 for _ in range(20001)]
    link=defaultdict(list)
    dq=deque()
    for edge in edges:
        link[edge[0]].append(edge[1])
        link[edge[1]].append(edge[0])
    visited[1]=1
    for i in link[1]:
        dq.append((i,1))
        
    dist,answer = 0,0
    
    while(dq):
        target,cnt=dq.popleft()
        if visited[target]: continue
        visited[target]=1
        if cnt>dist: dist=cnt; answer=1
        elif cnt==dist: answer+=1
        for _next in link[target]:
            if visited[_next]: continue
            else:
                dq.append((_next,cnt+1))
    return answer