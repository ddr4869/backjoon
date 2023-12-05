import sys

numberOfCrane=int(input())
weights=list(map(int, input().split()))
numberOfBox=int(input())
boxs=list(map(int, input().split()))
answer=0

weights.sort(reverse=True)
boxs.sort(reverse=True)

if weights[0]<boxs[0]:
    print(-1)
    sys.exit()

boxRemain=len(boxs)
while(len(boxs)):
    boxIndex=0
    removeCnt=0
    answer+=1
    for weight in weights:
        if boxIndex>=boxRemain:
            break
        while boxIndex<boxRemain and weight<boxs[boxIndex]:
            boxIndex+=1
        if boxIndex<boxRemain and weight>=boxs[boxIndex]:
            boxs[boxIndex]=0
            removeCnt+=1
            boxIndex+=1
        
    boxs=[i for i in boxs if i != 0]
    boxRemain-=removeCnt
print(answer)