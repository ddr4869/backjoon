import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [(0, 0)] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = (data[i], i + 1)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = (value, pos - self.n + 1)
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query_min(self):
        return self.tree[1][1]

n = int(input())
data = list(map(int, input().split()))
m = int(input())

tree = SegmentTree(data)

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 2:
        print(tree.query_min())
    elif query[0] == 1:
        tree.update(query[1] - 1, query[2])
