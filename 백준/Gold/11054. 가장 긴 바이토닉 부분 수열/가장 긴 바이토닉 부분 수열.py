import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
answer=1
dp=[[0,0] for _ in range(n)]
dp[0]=[1,1]
for i in range(1,n):
    left, right = 1, 1
    for j in range(0,i):
        if arr[j]<arr[i]:
            left = max(dp[j][0]+1, left)
            right = max(dp[j][0]+1, right)
        if arr[j]>arr[i]:
            right = max(dp[j][0]+1, right)
            right = max(dp[j][1]+1, right)
    dp[i]=[left,right]
    answer = max(right, answer)
print(answer)