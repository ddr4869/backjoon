import heapq
def solution(n, k, enemy):
    if k>=len(enemy):
        return len(enemy)
    heap=[]
    for i in range(k):
        heap.append(enemy[i])
    heapq.heapify(heap)
    heappop=heapq.heappop(heap)
    for i,v in enumerate(enemy):
        if i<k: continue
        if v>heappop:
            n-=heappop
            heapq.heappush(heap, v)
            heappop=heapq.heappop(heap)
        else:
            n-=v
        if n<0: return i
    return len(enemy)