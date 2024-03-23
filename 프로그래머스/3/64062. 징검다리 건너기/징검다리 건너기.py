def can_move(stones,target,k):
    stack=0
    for stone in stones:
        if stone<target: 
            stack+=1
            if stack==k: return False
        else:
            stack=0
    return True
    

def solution(stones, k):
    answer = 0
    max,min=0,200000
    for stone in stones:
        if stone>max: max=stone
        if stone<min: min=stone
    while(min<=max):
        target=(min+max)//2
        if can_move(stones,target,k):
            if target>answer: answer=target
            min=target+1
        else:
            max=target-1
    return answer