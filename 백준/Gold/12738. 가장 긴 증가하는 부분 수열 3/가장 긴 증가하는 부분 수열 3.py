import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
minimums=[arr[0]]
for num in arr:
    if minimums[-1] < num:
        minimums.append(num)
    else:
        minimums[bisect_left(minimums, num)] = num
print(len(minimums))