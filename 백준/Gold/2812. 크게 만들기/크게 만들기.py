import sys
from collections import deque
input = sys.stdin.readline
n,k=list(map(int, input().split()))
number=str(input().rstrip())
q=deque()
for i in number:
    if k and int(i)==0: 
        k-=1
        continue
    if not q: q.append(i)
    else:
        if k==0 or int(q[-1])>=int(i): 
            q.append(i)
        else:
            while(k and q and int(q[-1])<int(i)):
                q.pop()
                k-=1
            q.append(i)
if k!=0: q=list(q)[:-k]
print(''.join(q))