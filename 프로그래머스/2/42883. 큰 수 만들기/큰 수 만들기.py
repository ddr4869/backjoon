def solution(number, k):
    answer = ''
    length=len(number)
    cnt=0
    stack=[]
    for i,v in enumerate(number):
        while(cnt<k and stack and stack[-1]<v):
            stack.pop()
            cnt+=1
        stack.append(v)

    while(cnt<k):
        stack.pop()
        cnt+=1
    for i in stack:
        answer+=str(i)
    return answer