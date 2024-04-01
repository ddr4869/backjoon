import sys
from collections import deque
input = sys.stdin.readline
str=input().strip()
explode=input().strip()
q=[]
for i in str:
    q.append(i)
    if len(q)>=len(explode) and ''.join(q[-len(explode):])==explode:
        for i in range(len(explode)):
            q.pop()
print(''.join(q)) if q else print("FRULA")