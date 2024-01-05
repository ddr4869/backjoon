def solution(progresses, speeds):
    answer = []
    developed,length=0,len(progresses)
    while(developed<length):
        release=0
        for i in range(developed,length):
            progresses[i]+=speeds[i]
        while(developed<length):
            if progresses[developed]>=100: 
                release+=1
                developed+=1
            else: 
                if release: answer.append(release)
                break
    answer.append(release)
    return answer