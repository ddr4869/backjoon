from itertools import combinations

def solution(relation):
    answer=0
    row_len=len(relation)
    col_len=len(relation[0])
    keyComb=[]
    for i in range(1,col_len+1):
        keyComb+=list(combinations(range(col_len),i))
    
    candidate,unique=[],[]
    for keys in keyComb:
        candidate=set([tuple(rel[key] for key in keys) for rel in relation ])
        if len(candidate)==row_len: 
            flag=True
            for uni in unique:
                if set(keys) > set(uni):
                    flag=False
                    break
            if flag:
                unique.append(keys) 
                answer+=1
                
    return answer