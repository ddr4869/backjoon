# 프림
import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline
v,e=list(map(int, input().split()))
edges=defaultdict(list)
for _ in range(e):
    a,b,cost=list(map(int, input().split()))
    edges[a].append((cost,b))
    edges[b].append((cost,a))

h=[]; cnt=1
heapq.heappush(h, (0, 1))
visited=[False for _ in range(v+1)]
answer=0
while(h):
    cost,here= heapq.heappop(h)
    if visited[here]: continue
    visited[here]=True
    answer+=cost
    for next_cost,_next in edges[here]:
        if not visited[_next]:
            heapq.heappush(h, (next_cost,_next))
print(answer)