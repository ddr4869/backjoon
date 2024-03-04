def solution(targets):
    answer = 0
    end=1000000000
    targets.sort(key=lambda x:(x[0], x[1]))
    for target in targets:
        end=min(end, target[1])
        if target[0]>=end:
            answer+=1
            end=target[1]
    
    return answer+1