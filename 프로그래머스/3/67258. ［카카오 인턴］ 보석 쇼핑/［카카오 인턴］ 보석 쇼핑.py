from collections import defaultdict
def solution(gems):
    answer = []
    dict=defaultdict(int)
    pick=defaultdict(int)
    for gem in gems:
        dict[gem]+=1
    
    left,right=0,0
    for i,v in enumerate(gems):
        pick[v]+=1
        if pick.keys()==dict.keys():
            right=i; break
    
    answer = [left+1,right+1]
    while(right<len(gems)):
        while(left<right and pick[gems[left]]>1): 
            pick[gems[left]]-=1; left+=1
        if right-left < answer[1]-answer[0]: 
            answer=[left+1,right+1]
        right+=1
        if right<len(gems): pick[gems[right]]+=1 
    return answer