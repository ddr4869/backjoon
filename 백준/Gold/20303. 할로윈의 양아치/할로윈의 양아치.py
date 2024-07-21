import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX
        group_size[rootX] += group_size[rootY]
        group_candies[rootX] += group_candies[rootY]

n, m, k = map(int, input().split())
candies = [0] + list(map(int, input().split())) 
parent = list(range(n + 1))
group_size = [1] * (n + 1)
group_candies = candies[:]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n + 1):
    find(i)  

groups = []
for i in range(1, n + 1):
    if parent[i] == i and group_size[i] < k:
        groups.append((group_size[i], group_candies[i]))

dp = [0] * k
for size, candy in groups:
    for j in range(k - 1, size - 1, -1):
        dp[j] = max(dp[j], dp[j - size] + candy)

print(dp[k - 1])