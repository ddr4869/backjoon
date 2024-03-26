import heapq
def solution(operations):
    answer = []
    heapq_min=[]
    heapq_max=[]
    heap_size=0
    for oper in operations:
        if oper[0]=='I': 
            heapq.heappush(heapq_min, int(oper[2:]))
            heapq.heappush(heapq_max, -1*int(oper[2:]))
            heap_size+=1
        if oper[0]=='D':
            if heap_size>0: heap_size-=1
            if oper[2:]=='-1' and heapq_min: heapq.heappop(heapq_min)
            if oper[2:]=='1' and heapq_max: heapq.heappop(heapq_max)
        if heap_size==0:
            heapq_min=[]
            heapq_max=[]
    list_min=list(heapq_min)
    list_max=[-i for i in list(heapq_max)]
    answers=[]
    for i in list_min:
        if i in list_max:
            answers.append(i) 

    if not answers: return [0,0]
    answer.append(max(answers))            
    answer.append(min(answers))
    return answer