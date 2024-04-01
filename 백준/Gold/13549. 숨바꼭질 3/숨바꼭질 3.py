import sys
from collections import deque

n,k = list(map(int, input().split()))
def solve(k):
    if n>=k: return n-k
    dq=deque()
    dq.append((n,0)) if n!=0 else dq.append((1,1))
    visited=[0 for _ in range(200010)]
    while(dq):
        locate,cost=dq.popleft()
        if locate==k: return cost
        if locate<0 or locate>2*k or visited[locate] : continue
        visited[locate]=1
        dq.append((locate+1,cost+1))
        dq.append((locate-1,cost+1))
        dq.appendleft((locate*2,cost))

print(solve(k))