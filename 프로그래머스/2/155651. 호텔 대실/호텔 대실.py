def time_convert(time_str):
    hour=int(time_str[0:2])
    min=int(time_str[3:])
    return hour*60+min

def solution(book_time):
    answer = 0
    come=[0 for _ in range(len(book_time))]
    out=[0 for _ in range(len(book_time))]
    for idx, pair in enumerate(book_time):
        come[idx]=time_convert(pair[0])
        out[idx]=time_convert(pair[1])+10
    
    come.sort()
    out.sort()
    cIdx, oIdx, cnt = 0,0,0
    time=come[0]
    while(time<=come[-1]):
        while(oIdx<len(book_time) and time==out[oIdx]):
            cnt-=1; oIdx+=1
        while(cIdx<len(book_time) and time==come[cIdx]):
            cnt+=1; cIdx+=1
            if cnt>answer: answer+=1
        time+=1
    return answer