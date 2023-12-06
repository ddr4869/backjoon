import sys, heapq

input = sys.stdin.readline
sum,total=0,0
cardDecks=int(input())
cardSizes=[]
for i in range(cardDecks):
    cardSize=int(input())
    cardSizes.append(cardSize)
heapq.heapify(cardSizes)

while(cardDecks>1):
    first=heapq.heappop(cardSizes)
    second=heapq.heappop(cardSizes)
    sum=(first+second)
    total+=sum
    heapq.heappush(cardSizes, sum)
    cardDecks-=1

print(total)
