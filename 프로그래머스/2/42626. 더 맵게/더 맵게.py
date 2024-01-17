import heapq
def solution(scoville, K):
    answer = 0
    length=len(scoville)
    heapq.heapify(scoville)
    while(scoville[0]<K and length>=2):
        s1=heapq.heappop(scoville)
        s2=heapq.heappop(scoville)
        heapq.heappush(scoville, s1+2*s2)
        answer+=1
        length-=1
        
    return answer if scoville[0]>=K else -1