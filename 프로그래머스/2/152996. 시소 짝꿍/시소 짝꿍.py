from itertools import combinations
from collections import defaultdict
def solution(weights):
    answer=0
    dict=defaultdict(int)
    length=len(weights)
    for w in weights:
        dict[w]+=1
    for v in dict.values():
        if v>1:
            answer+= v*(v-1)//2
    comb=combinations(dict.keys(),2)

    for com in comb:
        x,y=com 
        if x<y: x,y=y,x
        if x*2==y*3 or x*2==y*4 or x*3==y*4: 
            answer+=dict[x]*dict[y]
    return answer