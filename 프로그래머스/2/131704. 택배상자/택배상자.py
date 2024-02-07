def solution(order):
    queue=[]
    answer,idx,target,start=0,0,0,1
    while(idx<len(order) and start<=len(order)):
        if order[idx]==start: 
            start+=1; idx+=1; answer+=1
        elif queue and queue[-1]==order[idx]:
            queue.pop(); idx+=1; answer+=1
        else:
            queue.append(start)
            start+=1
    while(queue and idx<len(order)):
        if queue[-1]==order[idx]:
            idx+=1; queue.pop(); answer+=1
        else: break
    return answer