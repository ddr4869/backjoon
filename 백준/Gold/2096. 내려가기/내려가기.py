import sys
input = sys.stdin.readline
n=int(input())
answer=[]
dp_max=[[0 for _ in range(3)] for _ in range(2)]
dp_min=[[0 for _ in range(3)] for _ in range(2)]
for i in range(n):
    a,b,c=list(map(int, input().split()))
    if i==0: dp_max[0]=[a,b,c]; dp_min[0]=[a,b,c]; continue
    dp_max[i%2][0]=max(dp_max[(i-1)%2][0],dp_max[(i-1)%2][1])+a
    dp_max[i%2][1]=max(max(dp_max[(i-1)%2][0],dp_max[(i-1)%2][1]),dp_max[(i-1)%2][2])+b
    dp_max[i%2][2]=max(dp_max[(i-1)%2][1],dp_max[(i-1)%2][2])+c
    dp_min[i%2][0]=min(dp_min[(i-1)%2][0],dp_min[(i-1)%2][1])+a
    dp_min[i%2][1]=min(min(dp_min[(i-1)%2][0],dp_min[(i-1)%2][1]),dp_min[(i-1)%2][2])+b
    dp_min[i%2][2]=min(dp_min[(i-1)%2][1],dp_min[(i-1)%2][2])+c
print(max(dp_max[(n-1)%2]), min(dp_min[(n-1)%2]))