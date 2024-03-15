import math
def solution(n, s):
    answer = []
    if n>s: return [-1]

    upper_num=s-n*(s//n)
    down_num=n-upper_num
    
    for i in range(down_num):
        answer.append(math.floor(s/n))
    for i in range(upper_num):
        answer.append(math.ceil(s/n))

    return answer