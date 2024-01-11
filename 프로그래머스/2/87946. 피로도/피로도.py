from itertools import permutations
def solution(k, dungeons):
    answer = 0
    perm=permutations(dungeons, len(dungeons))
    for case in perm:
        left,cnt=k,0
        for mustHave, consume in case:
            if left>=mustHave:
                left-=consume; cnt+=1
        answer=max(answer,cnt)
    return answer