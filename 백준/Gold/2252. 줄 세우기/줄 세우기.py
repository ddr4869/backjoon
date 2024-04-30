import sys
from collections import deque
input = sys.stdin.readline

n,m = list(map(int, input().split()))
indegree = [0] * (n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()
for i in range(1,n+1):
    if indegree[i]==0 and graph[i]:
        q.append(i)
        
while(q):
    now = q.popleft()
    result.append(now)
    for _next in graph[now]:
        indegree[_next] -= 1
        if indegree[_next] == 0:
            q.append(_next)

if len(result)<n:
    for i in range(1,n+1):
        if i not in result:
            result.append(i)
print(*result)