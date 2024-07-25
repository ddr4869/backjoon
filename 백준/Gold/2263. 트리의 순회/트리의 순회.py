import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
inorder_mid = [0 for _ in range(n+1)]
ans = []
cnt = 0
for i in range(n):
    inorder_mid[in_order[i]] = i

def pre_order(in_left, in_right, post_left, post_right):
    if in_left > in_right:
        return
    root = post_order[post_right]
    ans.append(root)
    if in_left == in_right:
        return
    if post_left >= post_right or in_left >= in_right:
        return
    in_mid = inorder_mid[root]
    post_mid = post_left + (in_mid - in_left)
    pre_order(in_left, in_mid - 1, post_left, post_mid - 1) 
    pre_order(in_mid + 1, in_right, post_mid, post_right - 1)

pre_order(0, n-1, 0, n-1)
print(*ans)