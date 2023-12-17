from collections import deque

def solution(queue1, queue2):
    q1Sum=sum(queue1)
    q2Sum=sum(queue2)
    total=(q1Sum+q2Sum)
    if total%2==1:
        return -1

    avg=total/2
    
    q1=deque(queue1)
    q2=deque(queue2)
    last=2*(len(queue1)+len(queue2))

    cnt=0
    while q1Sum!=avg and cnt<=last:
        if q1Sum<avg:
            atom=q2.popleft()
            q1.append(atom)
            q1Sum+=atom
        else:
            atom=q1.popleft()
            q2.append(atom)
            q1Sum-=atom
        cnt+=1
    
    if cnt>last:
        return -1
    answer = cnt
    return answer