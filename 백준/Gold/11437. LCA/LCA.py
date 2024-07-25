import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n = int(input())
tree = defaultdict(list)
depth = [0] * (n+1)
parent = [0] * (n+1)
visited = [False] * (n+1)

def make_depth():
    q = deque()
    q.append((1, 0))
    visited[1] = True
    while(q):
        node, level = q.popleft()
        for child in tree[node]:
            if not visited[child]:
                parent[child] = node
                depth[child] = level + 1
                q.append((child, level + 1))
                visited[child] = True
    
def lca(high, low):
    if depth[high] > depth[low]:
        high, low = low, high
    while depth[high] < depth[low]:
        low = parent[low]
    while high != low:
        high = parent[high]
        low = parent[low]
    print(high)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

make_depth()

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    lca(a,b)