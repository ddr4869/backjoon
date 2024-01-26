def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    remove=[]
    for i in lost:
        if i in reserve:
            remove.append(i)
    for i in remove:
        lost.remove(i)
        reserve.remove(i)
    answer = n-len(lost)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
    return answer