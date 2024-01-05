from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 1
    dq=deque()
    w,length,t,dq_len=0,len(truck_weights),0,0
    idx=0
    tmp=0

    while(idx<length):
        # out
        if len(dq)!=0 and (time-dq[0][0])==bridge_length:
            _,truck_w=dq.popleft()
            w-=truck_w

        # in
        if w+truck_weights[idx]<=weight:
            dq.append( (time,truck_weights[idx]) )
            w+=truck_weights[idx]
            idx+=1            
        
        time+=1
    if len(dq): time+= bridge_length-(time-dq[-1][0])
    return time