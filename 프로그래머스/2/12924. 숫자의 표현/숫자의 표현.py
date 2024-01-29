def solution(n):
    answer = 0
    for i in range(1,n+1):
        if ((i%2 and (n/i)%1==0) or (i%2==0 and (n/i)%1==0.5)) and (n/i)>=i//2+0.5: answer+=1;
    return answer