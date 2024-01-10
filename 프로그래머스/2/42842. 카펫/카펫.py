def solution(brown, yellow):
    x=3
    while(True):
        y=(brown+yellow)/x
        if y%1==0 and (x+y-2)==brown//2:
            return [x,y] if x>=y else [y,x]
        else: x+=1