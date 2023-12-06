import sys
import heapq

input = sys.stdin.readline
t=int(input())

while(t):
    sum,total=0,0
    fileSize=int(input())
    filePrices=list(map(int, input().split()))
    heapq.heapify(filePrices)
    #filePrices=heapq(filePrices_list)

    while(fileSize>1):
        first=heapq.heappop(filePrices)
        second=heapq.heappop(filePrices)
        sum=(first+second)
        total+=sum
        heapq.heappush(filePrices, sum)
        fileSize-=1
    
    print(total)
    t-=1