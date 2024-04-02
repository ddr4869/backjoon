from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
link=defaultdict(list)
answer=0
n,m,x=list(map(int, input().split()))
for i in range(m):
    start,arrive,cost=list(map(int, input().split()))
    link[start].append((cost,arrive))

def Dijkstra(start):
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
    return distance

to_home=Dijkstra(x)
for i in range(1,n+1):
    to_X=Dijkstra(i)[x]
    ans=to_X+to_home[i]
    if ans>answer: answer=ans
print(answer)