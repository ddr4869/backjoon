def solution(n, stations, w):
    answer = 0

    apartment=[]
    open=1
    for i in stations:
        if i-w <= open: open=i+w+1
        else:
            apartment.append((i-w)-open)
            open=i+w+1
    if open<=n: apartment.append(n+1-open)           
    
    for i in apartment:    
        answer+= (i-1)//(1+w*2) + 1
    
    return answer