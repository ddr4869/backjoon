N=int(input())
startTime=[]
endTime=[]
endIdx=0
cnt,maxCnt = 0,0

for i in range(N):
    start, end = map(int, input().split())
    startTime.append(start)
    endTime.append(end)

startTime.sort()
endTime.sort()

for time in startTime:
    while(time>=endTime[endIdx]):
        cnt-=1
        endIdx+=1  
    cnt+=1
    if cnt>maxCnt:
        maxCnt=cnt
    
print(maxCnt)