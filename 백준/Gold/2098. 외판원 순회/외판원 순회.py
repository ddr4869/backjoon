import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
cities = []
dp = defaultdict(tuple) 
for _ in range(n):
    cities.append(list(map(int, input().split())))

def dfs(now, route):
    if route == (1 << n) - 1:
        return cities[now][0] if cities[now][0] else 10e9
    if dp[(now, route)]:
        return dp[(now, route)]
    cost = 10e9
    for target in range(1, n):
        _next = route | (1 << target)
        visited = route & (1 << target)
        if cities[now][target] != 0 and not visited:
            cost = min(cost, dfs(target, _next) + cities[now][target])
    dp[(now, route)] = cost
    return cost

print(dfs(0, 1))