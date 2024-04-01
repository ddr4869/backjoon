from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
v,e = list(map(int, input().split()))
k=int(input())
path=defaultdict(list)

for i in range(e):
    start,arrive,cost = list(map(int, input().split()))
    path[start].append((cost,arrive))

distance=[10e9 for _ in range(v+1)]
distance[k]=0
q=[]
heapq.heappush(q,((0,k)))
while(q):
    cost,here=heapq.heappop(q)
    if distance[here]<cost: continue
    distance[here]=cost
    for next_cost, _next in path[here]:
        if cost+next_cost<distance[_next]:
            distance[_next]=cost+next_cost
            heapq.heappush(q,(cost+next_cost, _next))

for i in range(1,v+1):
    print(distance[i]) if distance[i]!=10e9 else print("INF")