def convert_time(str):
    return int(str[0:2])*60+int(str[3:])

def solution(plans):
    answer=[]
    for i in range(len(plans)):
        plans[i][1]=convert_time(plans[i][1])
        plans[i][2]=int(plans[i][2])
    plans.sort(key=lambda x:x[1])

    stack=[]
    stack.append([plans[0][2], plans[0][0]]) # (남은시간, 과목명)
    _next,time=1,plans[0][1]

    while(_next<len(plans)):
        come_time=plans[_next][1]-time
        if stack and come_time >= stack[-1][0]: # 기존 과제 먼저 끝남
            stack_time,subject = stack.pop()
            
            answer.append(subject)
            time+=stack_time

        else: # 새 과제가 먼저 옴
            if stack: stack[-1][0]-=come_time
            time=plans[_next][1]
            stack.append([ plans[_next][2], plans[_next][0] ])
            _next+=1
        
    for _ in range(len(stack)):
        answer.append(stack.pop()[1]) 
    return answer