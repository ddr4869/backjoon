import sys
from bisect import bisect_left
from collections import defaultdict

input = sys.stdin.readline
link = defaultdict(int)

n = int(input())
telephone = list(map(int, input().split()))
for i in range(n):
    link[i] = telephone[i]

arrivals = []
for start in sorted(link.keys()):
    arrive = link[start]
    pos = bisect_left(arrivals, arrive)
    if pos == len(arrivals):
        arrivals.append(arrive)
    else:
        arrivals[pos] = arrive

lis_length = len(arrivals)
arrivals.sort()
print(n - lis_length)