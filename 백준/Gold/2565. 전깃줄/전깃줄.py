import sys
from collections import defaultdict
link = defaultdict(int)
n = int(input())
for _ in range(n):
    start, arrive = map(int, input().split())
    link[start] = arrive

start = list(link.keys())
start.sort()
dp = [[0,0] for _ in range(start[-1] + 1)] #[arrive, stack]

for _from in start:
    stack = 1
    for i in range(1, _from):    
        if link[_from] > dp[i][0]:
            stack = max(stack, dp[i][1] + 1)
    dp[_from][0] = link[_from]    
    dp[_from][1] = stack

answer = []
for _, stack in dp:
    answer.append(stack)

print(n - max(answer))