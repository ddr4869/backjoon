import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
v,e=list(map(int, input().split()))
edges=[]
edges=defaultdict(list)
for i in range(e):
    a,b,cost=list(map(int, input().split()))
    edges[a].append((cost,b))
    edges[b].append((cost,a))
visited=[False for _ in range(v+1)]
h=[]; answer=[]
heapq.heappush(h, (0,1)) # cost, v

while(h):
    cost,here=heapq.heappop(h)
    if visited[here]==True: continue 
    visited[here]=True
    answer.append(cost)
    for next_cost,_next in edges[here]:
        if visited[_next]==False:
            heapq.heappush(h, (next_cost,_next))
print(sum(answer)-max(answer))