class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        if left > right:
            left, right = right, left
        left += self.n
        right += self.n + 1
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
n, m = map(int, input().split())
tree = SegmentTree(n)

answer = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update(b-1, c)
    elif a == 0:
        answer.append(tree.query(b-1, c-1))

for ans in answer:
    print(ans)
