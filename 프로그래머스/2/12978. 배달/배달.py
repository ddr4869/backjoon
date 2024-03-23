# 다익스트라
from collections import defaultdict
import heapq
def solution(N, road, K):
    dp=[10e12 for _ in range(N+1)]
    dict=defaultdict(list)
    for start,arrive,cost in road:
        dict[start].append((arrive,cost))
        dict[arrive].append((start,cost))
    stack=[]
    heapq.heappush(stack,(1,0)) # point, cost
    dp[1]=0
    while(stack):
        current,cost=heapq.heappop(stack)
        if dp[current] < cost: 
            continue
        next_list=dict[current]
        for _next,next_cost in next_list:
            if dp[_next]>cost+next_cost:
                dp[_next]=cost+next_cost
                heapq.heappush(stack,(_next,cost+next_cost))
    answer=0
    for i in range(1,N+1):
        if dp[i]<=K: answer+=1
    return answer