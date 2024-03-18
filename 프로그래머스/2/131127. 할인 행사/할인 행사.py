from collections import defaultdict
def check_answer(dict):
    for v in dict.values():
        if v>0: return False
    return True

def solution(want, number, discount):
    answer = 0
    dict=defaultdict(int)
    for i in range(len(want)):
        dict[want[i]]=number[i]

    for i in range(10):
        dict[discount[i]]-=1
    
    if check_answer(dict): 
        answer+=1

    left=0; right=10
    while(right<len(discount)):
        if discount[right] in dict.keys(): 
            dict[discount[right]]-=1
        if discount[left] in dict.keys(): 
            dict[discount[left]]+=1
        if check_answer(dict): 
            answer+=1
        right+=1 ; left+=1
    return answer
