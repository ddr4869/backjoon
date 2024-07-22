import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, k = map(int, input().split())
jewel, bags = [], []
for _ in range(n):
    m, v = map(int, input().split())
    jewel.append((m, v))
for _ in range(k):
    bags.append(int(input()))

jewel.sort(reverse=True)
bags.sort()

hq, ans, idx = [], 0, 0
while idx < len(bags) and jewel[-1][0] > bags[idx]:
    idx += 1

m, v = jewel.pop()
heappush(hq, (-v, m))

while idx < len(bags): # (m, v)
    while(jewel and jewel[-1][0] <= bags[idx]):
        m, v = jewel.pop()
        heappush(hq, (-v, m))
    if hq:
        ans -= heappop(hq)[0]
    idx += 1
print(ans)