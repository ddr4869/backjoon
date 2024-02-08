def solution(land):
    answer=0
    previous=[land[0][0],land[0][1],land[0][2],land[0][3]]
    current=[land[0][0],land[0][1],land[0][2],land[0][3]]
    for i in range(1,len(land)):
        current[0]=max(previous[1],previous[2],previous[3])+land[i][0]
        current[1]=max(previous[0],previous[2],previous[3])+land[i][1]
        current[2]=max(previous[0],previous[1],previous[3])+land[i][2]
        current[3]=max(previous[0],previous[1],previous[2])+land[i][3]
        for j in range(4):
            previous[j]=current[j]
    return max(current[0],current[1],current[2],current[3])