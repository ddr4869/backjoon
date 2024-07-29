import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
def dfs(i, sum):
    if i == len(arr):
        if sum == s:
            global ans
            ans += 1
        return
    dfs(i+1, sum + arr[i])
    dfs(i+1, sum)
dfs(0, 0)
if s == 0:
    ans -= 1
print(ans)