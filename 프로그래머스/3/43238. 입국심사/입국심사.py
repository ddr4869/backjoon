def solution(n, times):
    answer = 10e14
    times.sort()
    left,right=-1,times[-1]*n
    
    while(left+1<right):
        
        total=0
        target=(left+right)//2
        
        for time in times:
            total+=(target//time)         
        if total>=n:
            answer=min(answer,target)
            right=target
        else:   
            left=target
    return answer