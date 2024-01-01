def solution(msg):
    
    answer = []
        
    if len(msg)==1:
        answer.append(ord(msg)-64)
        return answer
    
    characters={}
    for i in range(0,26):
        characters[chr(65+i)]=i+1
    

    msg=list(msg)
    idx,wc,dict_len=0,0,27
    str=msg[0]
    
    for i,v in enumerate(msg):       
        if i==0:
            continue
        if str+v in characters: # hit
            str+=v
        else: # not hit
            answer.append(characters[str])
            characters[str+v]=dict_len
            dict_len+=1
            str=v
    answer.append(characters[str])
    
    return answer