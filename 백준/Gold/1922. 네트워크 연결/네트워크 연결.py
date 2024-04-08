import sys
input = sys.stdin.readline

def find(parent, a):
    if parent[a]==a: return a
    else: return find(parent, parent[a])

def union(parent, a, b):
    A=find(parent, a)
    B=find(parent, b)
    parent[A]=B

v=int(input())
e=int(input())
parent=[i for i in range(v+1)]

edges=[]
for i in range(e):
    a,b,cost=list(map(int, input().split()))
    edges.append((cost,a,b))
edges.sort()

answer=0
for cost,a,b in edges:
    if find(parent,a)!=find(parent,b):
        answer+=cost
        union(parent,a,b)
    else: continue
print(answer)