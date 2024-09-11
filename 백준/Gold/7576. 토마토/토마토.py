import sys
from collections import deque
input = sys.stdin.readline
maps=[]
m, n  = map(int, input().split())
for _ in range(n):
    maps.append(list(map(int, input().split())))
cnt, answer = 0, 10e8
q = deque()
ny, nx = [1,-1,0,0], [0,0,1,-1]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            cnt += 1
        if maps[i][j] == 1:
            q.append((i, j, 0))

while(q and cnt):
    y, x, ans = q.popleft()
    for i in range(4):
        if 0 <= y+ny[i] < n and 0 <= x+nx[i] < m and maps[y+ny[i]][x+nx[i]] == 0:
            cnt -= 1
            q.append((y+ny[i], x+nx[i], ans+1))
            maps[y+ny[i]][x+nx[i]] = 1
print(q[-1][2] if q else -1)
