import sys
from collections import defaultdict, deque
from itertools import combinations
input = sys.stdin.readline
n=int(input())
peoples=list(map(int, input().split()))
link=defaultdict(list)
for i in range(n):
    linked=list(map(int, input().split()))[1:]
    for j in range(len(linked)):
        linked[j]-=1
    link[i]=linked

total=sum(peoples)
answer=1000

def bfs(targets):
    visited=[0 for _ in range(n)]
    q=deque()
    q.append(targets[0])
    total=peoples[targets[0]]; cnt=1
    visited[targets[0]]=1
    while(q):
        here=q.popleft()
        for _next in link[here]:
            if visited[_next]==0 and _next in targets:
                visited[_next]=1
                total+=peoples[_next] ;cnt+=1
                q.append(_next)
    return total,cnt


for i in range(1,n//2+1):
    for first in list(combinations(range(n),i)):
        second=[i for i in range(n) if i not in first]
        t1,c1=bfs(first)
        t2,c2=bfs(second)
        if (c1+c2)==n and answer>abs(t1-t2):
            answer=abs(t1-t2) 
        
print(answer if answer!=1000 else "-1")