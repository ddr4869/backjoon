import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
tree = defaultdict(list)
n = int(input())
ans = -1
for i in range(1, n):
    parent, child, wieght = map(int, input().split())
    tree[parent].append((child, wieght))

def dfs(node):
    global ans
    dist = []
    for child, weight in tree[node]:
        dist.append(dfs(child) + weight)
    if len(dist) >= 3:
        dist.sort()
        dist = [dist[-1], dist[-2]]
    ans = max(ans, sum(dist))
    return max(dist) if dist else 0
dfs(1)
print(ans)