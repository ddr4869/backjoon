from collections import defaultdict
def solution(priorities, location):
    answer = 1
    p_dict=defaultdict(int)
    for i in priorities:
        p_dict[i]+=1
    
    p_list=[]
    for key,val in p_dict.items():
        p_list.append((key,val))
    p_list.sort(key= lambda x: -x[0])

    idx,length,cnt,here=0,len(priorities),0,0

    while(True):
        if idx==length: idx=0
        if priorities[idx]==p_list[here][0]:
            if idx==location: return answer
            answer+=1
            priorities[idx]=0
            cnt+=1
        if cnt==p_list[here][1]:
            here+=1
            cnt=0
        idx+=1