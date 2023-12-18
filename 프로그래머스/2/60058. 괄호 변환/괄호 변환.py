from collections import deque

def isRight(formula):
    cnt=0
    for i in formula:
        if i=='(': cnt+=1
        else: cnt-=1
        if cnt<0: return False
    
    if cnt==0: return True
    else: return False

def seperateUV(formula):
    if not formula:
        return None, None
    u,v,cnt ='','',0
    tmp=deque(formula)
    for i in formula:
        if i=='(': cnt+=1
        else:  cnt-=1    
        u+=tmp.popleft()
        if cnt==0:
            v=''.join(tmp)
            break
    return u,v

def process(w):
    # 1
    if not w:
        return ''
    # 2 u,v로 분리
    u,v=seperateUV(w)
    if isRight(u):
        return u+process(v) # 3-1
    else:
        answer='('+process(v)+')' #4-1~3
        u=u[1:-1]      
        return answer+''.join([')' if i=='(' else '(' for i in u])

def solution(p):
    if isRight(p):
        return p
    answer=process(p)
    return answer