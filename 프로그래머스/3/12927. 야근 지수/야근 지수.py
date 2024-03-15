import heapq
def solution(n, works):
    answer=0
    if n>=sum(works): return 0
    works.sort(key= lambda x:-x)
    
    idx=1
    while(n):
        if idx<len(works) and works[idx]==works[idx-1]:
            idx+=1
        else:
            for i in range(idx):
                if n: works[i]-=1; n-=1
                else: break 

    for i in works:
        answer+=i*i
    return answer 