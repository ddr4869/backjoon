import sys
input = sys.stdin.readline
n = int(input())
meetings=[]
for _ in range(n):
    meeting=tuple(map(int, input().split()))
    meetings.append(meeting)
# meetings.append((0,0))
dp=[0 for i in range(n+1)]

for i in range(n):
    if meetings[i][0]+i <= n:
        dp[i+meetings[i][0]] = max(dp[i+meetings[i][0]], dp[i]+meetings[i][1]) 
    dp[i+1] = max(dp[i], dp[i+1]) 

print(dp[-1])