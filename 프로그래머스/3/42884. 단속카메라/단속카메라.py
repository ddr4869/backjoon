def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    last_out=-300000
    for come,out in routes:
        if come>last_out: 
            answer+=1
            last_out=out
    return answer