import sys
import heapq
input = sys.stdin.readline
n=int(input())
edges_x=[]; edges_y=[]; edges_z=[]
for i in range(n):
    x,y,z=list(map(int, input().split()))
    edges_x.append((x,i))
    edges_y.append((y,i))
    edges_z.append((z,i))
edges_x.sort(); edges_y.sort(); edges_z.sort()
dist=[]
for i,v in enumerate(edges_x):
    if i==0: continue
    gap=edges_x[i][0]-edges_x[i-1][0] if edges_x[i][0]>edges_x[i-1][0] else edges_x[i-1][0]-edges_x[i][0]
    heapq.heappush(dist, (gap,edges_x[i-1][1],edges_x[i][1]))
for i,v in enumerate(edges_y):
    if i==0: continue
    gap=edges_y[i][0]-edges_y[i-1][0] if edges_y[i][0]>edges_y[i-1][0] else edges_y[i-1][0]-edges_y[i][0]
    heapq.heappush(dist, (gap,edges_y[i-1][1],edges_y[i][1]))
for i,v in enumerate(edges_z):
    if i==0: continue
    gap=edges_z[i][0]-edges_z[i-1][0] if edges_z[i][0]>edges_z[i-1][0] else edges_z[i-1][0]-edges_z[i][0]
    heapq.heappush(dist, (gap,edges_z[i-1][1],edges_z[i][1]))
parent=[i for i in range(1+n)]
rank=[i for i in range(1+n)]
answer=0

def find(parent, a):
    if parent[a]==a: return a
    else: return find(parent,parent[a])

def union(parent, a, b):
    rootA=find(parent, a)
    rootB=find(parent, b)
    if rootA < rootB:
        parent[rootB]=rootA
    else:
        parent[rootA]=rootB
while(dist):
    cost, start, arrive = heapq.heappop(dist)
    if find(parent, start) != find(parent, arrive):
        union(parent, start, arrive)
        answer+=cost
print(answer)
