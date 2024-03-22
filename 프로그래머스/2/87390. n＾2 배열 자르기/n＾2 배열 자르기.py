
def solution(n, left, right):
    answer = []
    leftI,leftJ=left//n,left%n
    
    for idx in range(left, right+1):
        i,j=idx//n,idx%n
        answer.append(max(i,j)+1)    
    return answer