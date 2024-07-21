import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))
ans = 100000

prefix_sum = [0 for _ in range(n+1)]
prefix_sum[1] = arr[1]
for i in range(2, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

left, right = 0, 1
for i in range(1, n+1):
    if prefix_sum[i] >= s:
        right = i
        break

while(right <= n):
    sum = prefix_sum[right] - prefix_sum[left]
    if sum >= s:
        ans = min(ans, right - left)
        left += 1
    else:
        right += 1

print(ans if ans != 100000 else 0)