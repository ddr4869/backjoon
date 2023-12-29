from collections import deque
def can_convert(begin, target):
    cnt=0
    for i in range(len(begin)):
        if begin[i]!=target[i]:
            cnt+=1
        if cnt>=2:
            return False
    return True if cnt==1 else False
    

def solution(begin, target, words):
    answer = 0
    if not target in words:
        return 0
    words_len = len(words)
    visit=[False for _ in range(words_len)]
    
    dq=deque()
    for idx, word in enumerate(words):
        if can_convert(begin, word):
            dq.append((idx,1))
    
    while(dq):
        _next,_cnt = dq.popleft()
        if words[_next]==target:
            return _cnt
        if visit[_next]==True:
            continue
        
        visit[_next]=True
        for idx, word in enumerate(words):
            if visit[idx]:
                continue
            if can_convert(words[_next], word):
                dq.append((idx,_cnt+1))
        
    return 0