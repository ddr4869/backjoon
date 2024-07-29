DIV = 1000000007
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [1] * (4 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = (self.tree[2 * i] * self.tree[2 * i + 1]) % DIV

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = (self.tree[2 * pos] * self.tree[2 * pos + 1]) % DIV

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 1
        while left < right:
            if left % 2 == 1:
                result = (result * self.tree[left] ) % DIV
                left += 1
            if right % 2 == 1:
                right -= 1
                result = (result * self.tree[right] ) % DIV
            left //= 2
            right //= 2
        return result

import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

tree = SegmentTree(data)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update(b-1, c)
    elif a == 2:
        print(tree.query(b-1, c))