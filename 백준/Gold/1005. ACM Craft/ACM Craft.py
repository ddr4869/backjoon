import sys
from collections import defaultdict, deque
input = sys.stdin.readline
t=int(input())

while(t):
    n,k=list(map(int, input().split()))
    #edges=[[0 for _ in range(n+1)] for _ in range(n+1)]
    edges=defaultdict(list)
    inEdge=[0 for _ in range(n+1)]
    dp=[0 for _ in range(n+1)]
    costs=[0]+list(map(int, input().split()))
    for _ in range(k):
        start,arrive=list(map(int, input().split()))
        edges[start].append(arrive)
        inEdge[arrive]+=1
    w=int(input())

    q=deque()
    for i,v in enumerate(inEdge):
        if i==0: continue
        if v==0: 
            q.append(i)
            dp[i]=costs[i]

    while(q):
        start=q.popleft()
        for _next in edges[start]:
            inEdge[_next]-=1
            dp[_next]=max(dp[start]+costs[_next], dp[_next])
            if inEdge[_next]==0: q.append(_next)
    print(dp[w])
    t-=1