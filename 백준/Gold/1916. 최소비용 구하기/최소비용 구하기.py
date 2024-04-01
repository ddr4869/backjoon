from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
n=int(input())
m=int(input())
link=defaultdict(list)
for i in range(m):
    start,arrive,cost=list(map(int, input().split()))
    link[start].append((cost,arrive))
start,arrive=list(map(int, input().split()))
distance=[10e9 for _ in range(n+1)]
distance[start]=0
q=[]
heapq.heappush(q,(0,start))
while(q):
    cost,here=heapq.heappop(q)
    if distance[here]<cost: continue
    distance[here]=cost
    for next_cost,_next in link[here]:
        if distance[_next]>cost+next_cost:
            distance[_next]=cost+next_cost
            heapq.heappush(q,(cost+next_cost,_next))
print(distance[arrive])