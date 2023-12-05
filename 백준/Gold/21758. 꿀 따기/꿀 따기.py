import sys
input = sys.stdin.readline

n = int(input())
honeys = list(map(int, input().split()))
honeysLen=len(honeys)
max=0

def rightHoneyBottle():
    global max
    for idx, val in enumerate(honeys):
        if idx==0 or idx==honeysLen-1:
            continue
        bee1=sum(honeys)-honeys[0]-val
        bee2=sum(honeys[idx+1:])
        total=bee1+bee2
        if max<total:
            max=total

def leftHoneyBottle():
    global max
    for idx, val in enumerate(honeys):
        if idx==0 or idx==honeysLen-1:
            continue
        bee1=sum(honeys)-honeys[-1]-val
        bee2=sum(honeys[:idx])
        total=bee1+bee2
        if max<total:
            max=total

def middleHoneyBottle():
    global max
    for idx, val in enumerate(honeys):
        if idx==0 or idx==honeysLen-1:
            continue
        total=sum(honeys[1:idx+1])+sum(honeys[idx:honeysLen-1])
        if max<total:
            max=total


rightHoneyBottle()
leftHoneyBottle()
middleHoneyBottle()
print(max)
