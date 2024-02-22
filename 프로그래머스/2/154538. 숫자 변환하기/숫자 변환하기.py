from collections import deque
def solution(x, y, n):
    dp=[0 for _ in range(y+1)]
    dq=deque()
    dq.append((y,0))
    while(dq):
        num,ans=dq.popleft()
        if num==x: return ans 
        if num<x or dp[num]: continue
        if num%2==0: dq.append((num//2,ans+1))
        if num%3==0: dq.append((num//3,ans+1))
        dq.append((num-n, ans+1))
    return -1