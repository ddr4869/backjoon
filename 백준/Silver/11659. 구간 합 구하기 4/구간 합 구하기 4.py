import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sums = [0] * n
sums[0] = arr[0]

for i in range(1, n):
    sums[i] = sums[i-1] + arr[i]
    
for _ in range(m):
    start, end = map(int, input().split())
    start -=2; end -=1
    if start<0:
        print(sums[end])
    else:
        print(sums[end]-sums[start])