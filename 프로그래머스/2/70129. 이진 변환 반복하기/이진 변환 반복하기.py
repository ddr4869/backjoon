def solution(s):
    answer = []
    cnt,zero=0,0
    while True:
        one=0
        for i in s:
            if i=='0': zero+=1
            else: one+=1
        cnt+=1
        if one==1: return [cnt,zero]
        s=bin(one)[2:]
            
    return answer