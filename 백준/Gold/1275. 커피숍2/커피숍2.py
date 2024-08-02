class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

import sys
input = sys.stdin.readline
n, q = map(int, input().split())
data = list(map(int, input().split()))
tree = SegmentTree(data)
while(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(tree.query(x-1, y))
    tree.update(a-1, b)
    q -= 1