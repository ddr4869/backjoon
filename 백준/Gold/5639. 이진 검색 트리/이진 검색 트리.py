import sys
from collections import defaultdict
from bisect import bisect_left
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
tree = defaultdict(list)
data = []
while True:
    try:
        x = int(input())
        data.append(x)
    except:
        break

def post_order(left, right):
    if left > right: 
        return
    root = data[left]
    idx = right + 1
    for i in range(left+1, right+1):
        if data[i] > root:
            idx = i
            break
    post_order(left+1, idx-1)
    post_order(idx, right)
    print(root)

post_order(0, len(data)-1)