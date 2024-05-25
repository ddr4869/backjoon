import sys
import heapq
input = sys.stdin.readline
n=int(input())
min_heap=[]
max_heap=[]

min_len, max_len=0, 0
for i in range(n):
    num=int(input())
    if i==0:
        heapq.heappush(min_heap, -num)
        min_len+=1
        print(-min_heap[0])
        continue
    if i==1:
        if -min_heap[0]>num:
            min_heap,max_heap = [-num], [-min_heap[0]]
        else:
            heapq.heappush(max_heap, num)
        max_len+=1
        print(-min_heap[0])
        continue

    if num < max_heap[0]:
        heapq.heappush(min_heap, -num)
        min_len+=1
    else:
        heapq.heappush(max_heap, num)
        max_len+=1

    if min_len-max_len >= 2:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        min_len-=1
        max_len+=1
    elif max_len>min_len:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        max_len-=1
        min_len+=1
    print(-min_heap[0])