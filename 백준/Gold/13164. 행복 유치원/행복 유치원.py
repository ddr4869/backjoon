numberOfKid, numberOfGroup=map(int, input().split())
kids=list(map(int, input().split()))
heightGap=[]

for idx, height in enumerate(kids):
    if idx==0:
        continue
    heightGap.append(kids[idx]-kids[idx-1])

heightGap.sort()

if numberOfGroup==1:
    print(kids[-1]-kids[0])
else:
    parseIdx=-(numberOfGroup-1)
    heightGap=heightGap[:parseIdx]
    print(sum(heightGap))