def calc_rock_dist(distance, rocks, n, middle):
    rocks.append(distance)
    previos=0
    for i in range(0,len(rocks)):
        rock_dist=rocks[i]-previos
        if rock_dist < middle:
            n-=1
            if n<0: return False 
        else:
            previos=rocks[i]
    return True
        
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    if len(rocks)==n: return distance
    left,right=-1,distance
    while(left+1<right):
        middle=(left+right)//2
        if calc_rock_dist(distance, rocks[:], n, middle):
            answer=max(answer,middle)
            left=middle
        else:
            right=middle
    return answer