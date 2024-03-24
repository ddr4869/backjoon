import heapq
from collections import defaultdict
def solution(n, roads, sources, destination):
    answer = []
    link=defaultdict(list)
    for start,arrive in roads:
        link[start].append(arrive)
        link[arrive].append(start)
    
    dp=[10e5 for _ in range(n+1)]
    dp[destination]=0
    stack=[]
    heapq.heappush(stack,(destination,0))
    while(stack):
        now,cost=heapq.heappop(stack)
        if dp[now]<cost:
            continue
        for _next in link[now]:
            if dp[_next]>cost+1:
                dp[_next]=cost+1
                heapq.heappush(stack, (_next,cost+1))
    for src in sources:
        answer.append(dp[src]) if dp[src]!=10e5 else answer.append(-1)
    return answer