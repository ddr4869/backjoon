from bisect import bisect_left, bisect_right
score_len=[0 for _ in range(24)]

def find_idx(part):
    idx=0
    if part[0]=="java": idx+=8
    if part[0]=="python": idx+=16
    if part[1]=="frontend": idx+=4
    if part[2]=="senior": idx+=2
    if part[3]=="pizza": idx+=1
    return idx

def calc_result(conditions, scores):
    if conditions[0]=='-': lang=(0,8,16)
    if conditions[0]=='cpp': lang=(0,)
    if conditions[0]=='java': lang=(8,)
    if conditions[0]=='python': lang=(16,)
    
    if conditions[1]=='-': part=(0,4)
    if conditions[1]=='backend': part=(0,)
    if conditions[1]=='frontend': part=(4,)
    
    if conditions[2]=='-': career=(0,2)
    if conditions[2]=='junior': career=(0,)
    if conditions[2]=='senior': career=(2,)

    if conditions[3]=='-': food=(0,1)
    if conditions[3]=='chicken': food=(0,)
    if conditions[3]=='pizza': food=(1,)
    
    ans=0
    for i in lang:
        for j in part:
            for k in career:
                for l in food:
                    idx=score_len[i+j+k+l] 
                    ans+=idx-bisect_left(scores[i+j+k+l], int(conditions[4]))
    return ans

def solution(info, query):
    answer = []    
    scores=[[] for _ in range(24)]
    for parts in info:
        part=parts.split(' ')
        scores[find_idx(part)].append(int(part[4]))
    
    for i,score in enumerate(scores):
        score.sort()
        score_len[i]=len(score)
        
    for qr in query:
        conditions=qr.split(' ')
        conditions=[i for i in conditions if not i=="and"]
        answer.append(calc_result(conditions, scores))
    
    return answer