import math
def is_permit(y,x,dist):
    return True if dist*dist>= y*y+x*x else False
    
def solution(k, d):
    cnt=d//k+1
    sum=cnt
    y=k*(d//k)
    for x in range(k,d+1,k):
        while(not is_permit(y,x,d) and y>=0):
            cnt-=1
            y-=k
        sum+=cnt
    return sum