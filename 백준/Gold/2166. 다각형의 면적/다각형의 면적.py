import sys
input = sys.stdin.readline
n = int(input())
locate=[]
for i in range(n):
    locate.append(list(map(int, input().split())))
locate.append(locate[0])
left=0; right=0
for i in range(1,n+1):
    left+=locate[i-1][0]*locate[i][1]
    right+=locate[i-1][1]*locate[i][0]
print(round(abs((left-right)/2), 1))