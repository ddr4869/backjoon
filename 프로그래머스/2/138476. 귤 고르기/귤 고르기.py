from collections import defaultdict
def solution(k, tangerine):
    dict=defaultdict(int)
    answer = 0
    tangerine.sort()
    for i in tangerine:
        dict[i]+=1

    sizes=[]
    for val in dict.values():
        sizes.append(val)
    sizes.sort(key=lambda x:-x)
    for i in sizes:
        answer+=1
        k-=i
        if k<=0: return answer
    return answer