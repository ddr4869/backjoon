numberOfCencer=int(input()) 
numberOfOffice=int(input()) 
cencers=list(map(int, input().split()))
heightGap=[]
cencers.sort()

for idx, height in enumerate(cencers):
    if idx==0:
        continue
    heightGap.append(cencers[idx]-cencers[idx-1])

heightGap.sort()

if numberOfOffice==1:
    print(cencers[-1]-cencers[0])
else:
    parseIdx=-(numberOfOffice-1)
    heightGap=heightGap[:parseIdx]
    print(sum(heightGap))