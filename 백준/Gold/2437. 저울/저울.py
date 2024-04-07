import sys
input = sys.stdin.readline
n=int(input())
weights=list(map(int, input().split()))
weights.sort()
if weights[0]!=1: print(1); sys.exit(0)
answer=0; num=1
for i,v in enumerate(weights):
    if i==0: continue
    if num+1<v: 
        answer=num+1; break
    num+=v
if answer==0: answer=sum(weights)+1
print(answer)