apeach=[]
MAX,N=0,0
ANSWER=[]

def is_ryan_win(ryan):
    global MAX, ANSWER
    apeach_total, ryan_total = 0,0
    for i in range(11):
        if not (apeach[i]==0 and ryan[i]==0):
            if apeach[i]>=ryan[i]:
                apeach_total+=(10-i)
            else:
                ryan_total+=(10-i)
    if ryan_total>apeach_total:
        
        if ryan_total-apeach_total>MAX:
            MAX=ryan_total-apeach_total
            ANSWER=ryan
            return ryan_total
        elif ryan_total-apeach_total==MAX:
            for i in range(11):
                if ryan[10-i]>ANSWER[10-i]:
                    ANSWER=ryan
                    return MAX
                elif ryan[10-i]<ANSWER[10-i]:
                    return MAX
            return MAX
    return -1

def solve(ryan, target, arrow_left):
    if arrow_left<0:
        return -1 
    if target==0:
        ryan[10]=arrow_left
        return is_ryan_win(ryan)
    if arrow_left==0:
        return is_ryan_win(ryan)
    ryan_=ryan[:] 
    ryan_[10-target]+=(apeach[10-target]+1)
    return max(solve(ryan_, target-1, arrow_left-(apeach[10-target]+1)), 
               solve(ryan, target-1, arrow_left))
    

def solution(n, info):
    global apeach, ANSWER, N
    apeach,N=info,n
    ryan=[0 for _ in range(11)]
    sum=solve(ryan,10,n)
    if sum<=0:
        return [-1]
    return ANSWER