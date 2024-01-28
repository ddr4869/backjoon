from collections import defaultdict
import heapq
def solution(n, costs):
    answer = 0
    dict=defaultdict(list)
    dist,visited,cnt,start,startIdxA,startIdxB=[],[0 for _ in range(n)],2,1e9,0,0
    
    for a,b,cost in costs:
        if a>b: a,b=b,a
        dict[a].append((cost,b))
        dict[b].append((cost,a))
        if cost<start:
            start=cost
            startIdxA=a
            startIdxB=b
    visited[startIdxA]=1
    visited[startIdxB]=1
    for i in dict[startIdxA]:
        heapq.heappush(dist, i)
    for i in dict[startIdxB]:
         heapq.heappush(dist, i)
    answer+=start
    
    while(cnt<n):
        next_=heapq.heappop(dist)
        if visited[next_[1]]: continue # 이미 방문시
        answer+=next_[0]
        visited[next_[1]]=1
        for i in dict[next_[1]]:
            if visited[i[1]]==0:
                heapq.heappush(dist,i)
        #dist+=dict[next_[1]]
        cnt+=1
    return answer