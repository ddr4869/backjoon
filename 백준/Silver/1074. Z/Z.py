import math
n,r,c = list(map(int, input().split()))
answer=0
n-=1
while(n>=0 and (r or c)):
    size=math.pow(2,n)
    if size>r and size<=c:  # 2사분면
        c-=size
        answer+=(size*size)
    elif size<=r and size>c: # 3사분면
        r-=size
        answer+=2*(size*size)
    elif size<=r and size<=c: # 4사분면
        r-=size; c-=size
        answer+=3*(size*size)
    n-=1
print(int(answer))