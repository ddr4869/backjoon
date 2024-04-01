n,m,r = list(map(int, input().split()))
answer=0
items=list(map(int, input().split()))
link=[[16 for _ in range(n)] for _ in range(n)]
for i in range(r):
    start,arrive,cost=list(map(int, input().split()))
    link[start-1][arrive-1]=cost
    link[arrive-1][start-1]=cost

for i in range(n):
    link[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if link[i][j]>link[i][k]+link[k][j]:
                link[i][j]=link[i][k]+link[k][j]
for i in range(n):
    sum=0
    for j in range(n):
        if link[i][j]<=m: sum+=items[j]
    if sum>answer: answer=sum
print(answer)