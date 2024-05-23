cnt=0

def dfs(numbers, target, idx, sum):
    global cnt
    if sum==target:
        cnt+=1
        return
    elif sum>target:
        return
    if idx>=len(numbers):
        return
    dfs(numbers, target, idx+1, sum+numbers[idx])
    dfs(numbers, target, idx+1, sum)
    
def solution(numbers, target):
    global cnt
    numbers_sum=sum(numbers)
    target=numbers_sum-target
    if target<=0 or target%2 :
        return 0
    dfs(numbers, target/2, 0, 0)
    return cnt
