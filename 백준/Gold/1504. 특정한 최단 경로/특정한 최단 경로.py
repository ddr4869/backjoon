from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
n,e = list(map(int, input().split()))
path=defaultdict(list)
for i in range(e):
    start,arrive,cost = list(map(int, input().split()))
    path[start].append((cost,arrive))
    path[arrive].append((cost,start))

def dijkstra(start,arrive):
    distance=[10e9 for _ in range(n+1)]
    distance[start]=0
    q=[]
    heapq.heappush(q, (0,start))
    while(q):
        cost,here=heapq.heappop(q)
        if cost>distance[here]: continue
        distance[here]=cost
        for next_cost,_next in path[here]:
            if distance[_next]>cost+next_cost:
                distance[_next]=cost+next_cost
                heapq.heappush(q,(cost+next_cost,_next))
    return distance[arrive]

v1,v2 = list(map(int, input().split()))

answer=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
answer=min(answer,dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n))
if e==0 or answer>=10e9: answer=-1
print(answer)