from collections import deque
def is_right(dq):
    stack=[]
    open=['[','(','{']
    cnt=0
    for bracket in dq:
        if bracket in open:
            stack.append(bracket)
            cnt+=1
        else:
            if cnt==0: return False
            if bracket==']' and stack[-1]!='[' : return False
            if bracket=='}' and stack[-1]!='{' : return False
            if bracket==')' and stack[-1]!='(' : return False
            stack.pop()
            cnt-=1
    return True if cnt==0 else False

def solution(s):
    answer = 0
    dq=deque(s)
    
    for i in range(len(s)):
        answer+= is_right(dq)
        dq.rotate(1)
        
    return answer