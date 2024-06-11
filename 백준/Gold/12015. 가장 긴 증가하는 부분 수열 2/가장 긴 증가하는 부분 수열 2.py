import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
minimums=[arr[0]]

def apply_dp(target):
    left, right = 0, len(minimums)-1
    if target > minimums[right]:
        minimums.append(target)
        return
    if target < minimums[0]:
        minimums[0] = target

    while(left + 1 < right):
        mid = (left + right)//2
        if minimums[mid] == target:
            return 
        elif minimums[mid] > target:
            right = mid
        elif minimums[mid] < target:
            left = mid
    
    if target > minimums[left] and target < minimums[left+1]:
        minimums[left+1] = target
    return 


for i in range(1, n):
    apply_dp(arr[i])

print(len(minimums))
