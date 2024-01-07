def solution(prices):
    answer = [0 for _ in range(len(prices))]
    dq=[]
    for idx,price in enumerate(prices):
        while(True):
            if len(dq)==0 or price>=dq[-1][0]: 
                dq.append((price,idx))
                break
            else:
                _,dq_idx=dq.pop()
                answer[dq_idx]=idx-dq_idx
                
    for price,idx in dq:
        answer[idx]=len(prices)-1-idx

    return answer