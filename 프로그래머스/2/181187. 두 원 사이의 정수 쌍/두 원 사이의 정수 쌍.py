import math
def solution(r1, r2):
    # r2 > r1
    if r1>r2: r1,r2=r2,r1
    answer = 0
    for x in range(1,r2+1):
        y1_=r1*r1-x*x if x<r1 else 0
        y2_=r2*r2-x*x if x<r2 else 0
        y1= math.sqrt(y1_)
        y2= math.sqrt(y2_)
        y1=math.ceil(y1); y2=math.floor(y2) 
        answer+=(y2-y1+1)

    return answer*4