from collections import defaultdict, deque
def solution(n, wires):
    link=defaultdict(list)
    answer = 100
    for v1,v2 in wires:
        link[v1].append(v2)
        link[v2].append(v1)
    
    for v1,v2 in wires:
        link[v1].remove(v2)
        dq=deque([v1])
        visited=[False for _ in range(n+1)]
        visited[v1]=True
        cnt=1
        while(dq):
            here=dq.popleft()
            for _next in link[here]:
                if not visited[_next]:
                    dq.append(_next)
                    visited[_next]=True
                    cnt+=1
        answer=min(answer, abs(n-2*cnt))
        link[v1].append(v2)
    return answer