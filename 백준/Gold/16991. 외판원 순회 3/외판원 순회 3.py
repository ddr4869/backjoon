import sys
import math
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
coordinate = []
cities = [[0 for _ in range(n)] for _ in range(n)]
dp = defaultdict(tuple) 
for _ in range(n):
    coordinate.append(list(map(int, input().split())))

def dist(y1, y2, x1, x2):
    return math.sqrt((y1-y2)*(y1-y2)+(x1-x2)*(x1-x2))

def convert_locate():
    for i in range(n):
        for j in range(i+1, n):
            cities[i][j] = dist(coordinate[i][0], coordinate[j][0], coordinate[i][1], coordinate[j][1])
            cities[j][i] = dist(coordinate[i][0], coordinate[j][0], coordinate[i][1], coordinate[j][1])

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

convert_locate()
print(dfs(0, 1))
