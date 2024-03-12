import heapq
def solution(numbers):
    answer=[-1 for _ in range(len(numbers))]
    stack=[]
    for i,v in enumerate(numbers):
        if not stack:
            heapq.heappush(stack, (v,i))
        else:
            while(stack and v>stack[0][0]):
                _,idx=heapq.heappop(stack)
                answer[idx]=v
            heapq.heappush(stack, (v,i))
    return answer