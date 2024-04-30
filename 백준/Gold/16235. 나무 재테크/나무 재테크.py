import sys
from collections import deque
input = sys.stdin.readline

n,m,k = list(map(int, input().split()))
maps = [[5 for _ in range(n)] for _ in range(n)]
add_energy = []
for i in range(n):
    add_energy.append(list(map(int, input().split())))

trees = [[deque() for _ in range(n)] for _ in range(n)]
for i in range(m):
    y,x,z = list(map(int, input().split()))
    y -= 1 ; x -= 1
    trees[y][x].append(z)

five_tree = [[0 for _ in range(n)] for _ in range(n)]

near=[(-1,-1),(-1,0),(-1,1),
      (0,-1),(0,1),
      (1,-1),(1,0),(1,1)]

while(k):
    for y in range(n):
        for x in range(n):
            # spring & summer
            summer_energy = 0
            five_trees = 0
            dq = trees[y][x]
            _next = deque()
            while(True):
                if dq and maps[y][x] >= dq[0]:
                    tree_age = dq.popleft()
                    maps[y][x] -= tree_age
                    _next.append(tree_age + 1)
                    if (tree_age+1) % 5 == 0:
                        five_trees += 1
                else:
                    for death_age in dq:
                        summer_energy += death_age//2 
                    maps[y][x] += summer_energy
                    break
            trees[y][x] = _next
            five_tree[y][x] = five_trees
    # autumn
    for y in range(n):
        for x in range(n):
            for ny, nx in near:
                if 0 <= y+ny < n and 0 <= x+nx < n:
                    for _ in range(five_tree[y][x]):
                        trees[y+ny][x+nx].appendleft(1)
    # winter
    for i in range(n):
        for j in range(n):
            maps[i][j] += add_energy[i][j]
    k-=1

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)
