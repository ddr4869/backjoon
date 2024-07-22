import sys
from bisect import bisect_left
from collections import defaultdict

input = sys.stdin.readline
link = defaultdict(int)

n = int(input())
for _ in range(n):
    start, arrive = map(int, input().split())
    link[start] = arrive

starts = sorted(link.keys())

arrivals = []
prev_indices = [-1] * len(starts)
lis_indices = []

for i, start in enumerate(starts):
    arrive = link[start]
    pos = bisect_left(arrivals, arrive)
    
    if pos == len(arrivals):
        arrivals.append(arrive)
        if pos > 0:
            prev_indices[i] = lis_indices[-1]
        lis_indices.append(i)
    else:
        arrivals[pos] = arrive
        if pos > 0:
            prev_indices[i] = lis_indices[pos - 1]
        lis_indices[pos] = i

lis_length = len(arrivals)
lis_elements = []
index = lis_indices[-1]
while index != -1:
    lis_elements.append(starts[index])
    index = prev_indices[index]

lis_elements = set(lis_elements)

to_remove = sorted(set(starts) - lis_elements)

print(n - lis_length)
for start in to_remove:
    print(start)
