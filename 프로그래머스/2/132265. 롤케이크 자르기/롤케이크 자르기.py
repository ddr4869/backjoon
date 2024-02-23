from collections import defaultdict
def solution(topping):
    answer,idx=0,1
    left_dict=defaultdict(int)
    right_dict=defaultdict(int)
    left_dict[topping[0]]+=1
    for i in range(1,len(topping)):
        right_dict[topping[i]]+=1

    while(idx<len(topping)-1):
        left_dict[topping[idx]]+=1
        right_dict[topping[idx]]-=1
        if right_dict[topping[idx]]==0:
            del right_dict[topping[idx]]
        if len(left_dict.keys())==len(right_dict.keys()):
            answer+=1
        if len(left_dict.keys())>len(right_dict.keys()):
            return answer
        idx+=1