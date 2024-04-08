def find(parent, x):
    if parent[x] == x: return x
    else: return find(parent, parent[x])

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    parent[rootY] = rootX

v,e=list(map(int, input().split()))
parent=[i for i in range(v+1)] 
edges=[]; answer=0
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
for cost,a,b in edges:
    if find(parent, a) != find(parent, b):
      union(parent, a, b)
      answer+=cost
print(answer)