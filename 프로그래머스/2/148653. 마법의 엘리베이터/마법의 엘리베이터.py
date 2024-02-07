import math
def solve(list_storey, idx, up, ans):
    while(idx<len(list_storey)):
        val=list_storey[idx]
        if up: val+=1
        if val==5:
            return min(solve(list_storey, idx+1, False, ans+val), solve(list_storey, idx+1, True, ans+10-val))
        elif val<5:
            ans+=val
            up=False
            idx+=1
        else:
            ans+=10-val
            up= True
            idx+=1
    return ans+1 if up else ans

def solution(storey):
    str_storey=str(storey)
    list_storey=[]
    for i in str_storey:
        list_storey.append(int(i))
    list_storey.reverse()
    up=False
    return solve(list_storey, 0, up, 0)