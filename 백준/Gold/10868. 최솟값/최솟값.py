INF=10**10
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.min = [0] * (4 * self.n)
        self.max = [INF] * (4 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.min[self.n + i] = data[i]
            self.max[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.min[i] = min(self.min[2 * i], self.min[2 * i + 1])
            self.max[i] = max(self.max[2 * i], self.max[2 * i + 1])

    def query_min(self, left, right):
        left += self.n
        right += self.n
        result = INF
        while left < right:
            if left % 2 == 1:
                result = min(result, self.min[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                result = min(result, self.min[right])
            left //= 2
            right //= 2
        return result

    def query_max(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2 == 1:
                result = max(result, self.max[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                result = max(result, self.max[right])
            left //= 2
            right //= 2
        return result


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

tree = SegmentTree(data)

for _ in range(m):
    left, right = map(int, input().split())
    print(tree.query_min(left - 1, right))