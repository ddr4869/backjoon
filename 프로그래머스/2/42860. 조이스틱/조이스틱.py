def solution(name):
    answer = 0
    notA=[]
    for c in name:
        if ord(c)<=78: answer+= (ord(c)-65)
        else: answer+= (91-ord(c)) 
    for i in range(len(name)):
        if name[i]!='A': notA.append(i)
    if 'A' not in name:
        return answer+len(name)-1
    if len(notA)==1:
        return answer+notA[0]

    move=21
    for i in range(len(notA)):
        if i==0:
            start=0
            last=notA[0]
        else:
            start=notA[i-1]
            last=notA[i]
        move= min(min(min(len(name)-1, 2*start+len(name)-last), start+2*(len(name)-last)),move)
    if notA:
        start=notA[-1]
        last=len(name)
        move= min(min(min(len(name)-1, 2*start+len(name)-last), start+2*(len(name)-last)),move)
    else: move=0
    
    return answer+move