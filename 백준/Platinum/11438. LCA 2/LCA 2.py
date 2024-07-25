import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(200000)

n = int(input())
tree = defaultdict(list)
depth = [0] * (n+1)
parent = [[0] * 18 for _ in range(n+1)]
visited = [False] * (n+1)

# 트리 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node, dep):
    visited[node] = True
    depth[node] = dep
    for next_node in tree[node]:
        if not visited[next_node]:
            parent[next_node][0] = node
            dfs(next_node, dep + 1)

dfs(1, 0)

for j in range(1, 18):
    for i in range(1, n + 1):
        parent[i][j] = parent[parent[i][j-1]][j-1]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    diff = depth[u] - depth[v]
    for i in range(18):
        if (diff >> i) & 1:
            u = parent[u][i]

    if u == v:
        return u

    for i in range(17, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]

    return parent[u][0]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
