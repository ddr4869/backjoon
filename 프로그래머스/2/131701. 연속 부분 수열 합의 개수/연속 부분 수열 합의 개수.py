from collections import defaultdict
def solution(elements):
    answers=defaultdict(bool)
    for i in range(1, len(elements)+1):
        total=0
        for j in range(0,i):
            total += elements[j]
        answers[total]=True
        for k in range(0,len(elements)):
            total -= elements[k]
            total += elements[(k+i)%len(elements)]
            answers[total]=True
    return len(answers.keys())