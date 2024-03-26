def solution(sequence):
    answer = 0
    sum=0
    sign=1
    for seq in sequence:
        sum+=(seq*sign)
        answer=max(answer,sum)
        if sum<0: sum=0
        sign*=-1
    sign=-1
    sum=0
    for seq in sequence:
        sum+=(seq*sign)
        answer=max(answer,sum)
        if sum<0: sum=0
        sign*=-1
    return answer