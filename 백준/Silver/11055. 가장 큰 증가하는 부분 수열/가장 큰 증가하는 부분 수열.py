import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = arr[0]
dp = [0 for _ in range(len(arr))]
dp[0] = arr[0]
for i in range(1, len(arr)):
    target = 0
    for j in range(0, i):
        if arr[j] < arr[i]:
            target = max(target, dp[j])
    dp[i] = target + arr[i]
print(max(dp))