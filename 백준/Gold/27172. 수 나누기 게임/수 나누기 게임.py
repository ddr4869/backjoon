import sys
import math
from collections import defaultdict
nums = defaultdict(int)
n = int(input())
players = list(map(int, input().split()))
for player in players:
    nums[player] = 0
scores = [0 for _ in range(n)]

def find_divide(n):
    div = [1]
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            div.append(i)
            if n // i not in div:
                div.append(n // i)
    return div

for p in players:
    div = find_divide(p)
    for d in div:
        if d in nums:
            nums[d] += 1
            nums[p] -= 1

print(' '.join(map(str, list(nums.values()))))