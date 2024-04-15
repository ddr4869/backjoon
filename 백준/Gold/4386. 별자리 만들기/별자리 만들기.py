import sys
import math
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
locate=[]
for i in range(n):
    locate.append(list(map(float, input().split())))

distance=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        distance[i][j]=distance[j][i]= math.sqrt(math.pow(locate[i][0]-locate[j][0], 2)+math.pow(locate[i][1]-locate[j][1], 2))

h=[]
heappush(h, (0, 0))
visited=[False for _ in range(n)]
answer=0
while(h):
    cost, here = heappop(h)
    if visited[here]: continue
    visited[here]=True
    answer+=cost
    for _next,dist in enumerate(distance[here]):
        if here==_next: continue
        if visited[_next]==False:
            heappush(h, (dist, _next))

print(round(answer, 2))