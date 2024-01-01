def remove(cap, custom):
    cnt=0
    while(custom):
        dist,boxes=custom.pop()
        cnt+=boxes
        if cnt>cap:
            custom.append((dist, cnt-cap))
            break
        elif cnt==cap:
            break

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries=[(i+1,v) for i, v in enumerate(deliveries) if v!=0 ]
    pickups=[(i+1,v) for i, v in enumerate(pickups) if v!=0 ]
    
    while(deliveries or pickups):
        if not deliveries: answer += pickups[-1][0]*2 
        elif not pickups: answer += deliveries[-1][0]*2
        else: answer += max(deliveries[-1][0], pickups[-1][0])*2
        remove(cap, deliveries)
        remove(cap, pickups)
    return answer