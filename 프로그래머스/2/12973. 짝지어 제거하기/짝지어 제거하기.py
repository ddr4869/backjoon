def solution(s):
    answer = 0
    queue=[]
    queue_len=0
    for i in s:
        if queue_len==0:
            queue.append(i)
            queue_len+=1
        else:
            top=queue[-1]
            if i!=top: 
                queue.append(i)
                queue_len+=1
            else:
                queue.pop()
                queue_len-=1
    if queue_len: return 0
    else: return 1