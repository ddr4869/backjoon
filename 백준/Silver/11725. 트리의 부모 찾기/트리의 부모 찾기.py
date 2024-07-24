import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
tree = defaultdict(list)
n = int(input())
parent = [0 for _ in range(n+1)]
for i in range(1, n):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
def dfs(node):
    for child in tree[node]:
        if parent[child]: 
            continue            
        parent[child] = node
        dfs(child)
dfs(1)
for p in parent[2:]:
    print(p)