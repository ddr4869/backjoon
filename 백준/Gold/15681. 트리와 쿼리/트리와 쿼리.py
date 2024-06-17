import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, r, q = map(int, input().split())
info = defaultdict(list)

for _ in range(n - 1):
    left, right = map(int, input().split())
    info[left].append(right)
    info[right].append(left)

dp = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    dp[node] = 1
    for child in info[node]:
        if not visited[child]:
            dp[node] += dfs(child)
    return dp[node]

dfs(r)

for _ in range(q):
    node = int(input())
    print(dp[node])
