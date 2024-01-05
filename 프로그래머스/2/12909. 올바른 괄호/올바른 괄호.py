def solution(s):
    idx,queue,length=0,[],0
    while(idx<len(s)):
        if s[idx]=='(': queue.append("("); length+=1
        else:
            if length==0 or queue[-1]!='(': return False
            else: queue.pop; length-=1
        idx+=1
    return True if length==0 else False