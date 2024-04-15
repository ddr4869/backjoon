import sys
input = sys.stdin.readline

n = int(input())
scores=list(map(int, input().split()))

def solve():
    if scores[0]*scores[-1]>=0: 
        if scores[-2]<0:
            return [scores[-2], scores[-1]]
        else:
            return [scores[0], scores[1]]
    left=0
    right=len(scores)-1
    answer=2000000000
    pnt=[]
    while left<right:
        gap=scores[right]+scores[left]
        if gap>=0:
            if answer>gap:                
                answer=gap
                pnt=[scores[left],scores[right]]
            right-=1
        else:
            if answer> (-gap):
                answer= (-gap)
                pnt=[scores[left],scores[right]]
            left+=1
    return pnt

ans=solve()
print(ans[0], ans[1])