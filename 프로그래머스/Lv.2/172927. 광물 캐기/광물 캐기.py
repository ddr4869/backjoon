from itertools import permutations
from collections import defaultdict
def solution(picks, minerals):
    answer,cnt = 1e8,0
    dict=defaultdict(int)
    pick=[]
    need=len(minerals)//5+1 if len(minerals)%5!=0 else len(minerals)//5

    for i, p in enumerate(picks):
        for j in range(p):
            if cnt<need:
                pick.append(i+1)
                cnt+=1
            else: break
        if cnt>=need: break
    
    pickup= len(pick) if len(pick)<need else need
    per=permutations(pick,pickup)
    
    for i in per:
        dict[i]=1
    
    for keys in dict.keys():
        idx,cnt,total=0,0,0
        for k in keys:
            while(cnt<5):
                if idx>=len(minerals):
                    if total: answer=min(answer,total)
                    break
                if k==2 and minerals[idx]=="diamond": total+=5
                elif k==3 and minerals[idx]=="diamond": total+=25
                elif k==3 and minerals[idx]=="iron": total+=5
                else: 
                    total+=1
                    if total>answer: break
                idx+=1; cnt+=1
            cnt=0
        if total: answer=min(answer,total)
    return answer