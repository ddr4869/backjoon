def solution(word):
    target=[]
    for w in word:
        if w=='A': target.append(1)
        if w=='E': target.append(2)
        if w=='I': target.append(3)
        if w=='O': target.append(4)
        if w=='U': target.append(5)
    
    while(len(target)<5):
        target.append(0)

    thisword=[1,0,0,0,0]
    idx,cnt=0,1
    while(True):
        if thisword==target: return cnt
        if idx<4:
            thisword[idx+1]=1
            idx+=1; cnt+=1
        else:
            thisword[idx]+=1
            if thisword[idx]==6: # 끝이 U
                tmp=idx
                while(tmp>=0 and thisword[tmp]>5):
                    thisword[tmp]=0
                    tmp-=1
                    thisword[tmp]+=1
                idx=tmp
            cnt+=1