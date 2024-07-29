import sys
input = sys.stdin.readline
n = int(input())
k = int(input())

def find(mid, n):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)
    return cnt

def solve(n, k):
    left, right = 1, n * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if find(mid, n) >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

print(solve(n, k))