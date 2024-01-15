import math
def calc(num):
    if num==1: return 0
    end=int(math.sqrt(num)//1)
    max=1
    for i in range(2,end+1):
        if num%i == 0:
            max=i
            if num//i<=10000000: 
                return num//i
    return max

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(calc(i))
    return answer
