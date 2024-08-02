import sys
INF=10**9
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [(INF, INF)] * (2 * self.n)
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

    def query_min(self, left, right):
        left += self.n - 1
        right += self.n
        result = (INF, INF)
        while left < right:
            if left % 2 == 1:
                result = min(result, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                result = min(result, self.tree[right])
            left //= 2
            right //= 2
        return result[0]

n = int(input())
data = list(map(int, input().split()))
m = int(input())

tree = SegmentTree(data)

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 2:
        print(tree.query_min(query[1], query[2]))
    elif query[0] == 1:
        tree.update(query[1] - 1, query[2])
