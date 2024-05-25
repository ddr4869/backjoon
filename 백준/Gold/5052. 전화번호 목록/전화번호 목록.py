import sys
from collections import deque
input = sys.stdin.readline
t=int(input())
while(t):
    n=int(input())
    numbers=[]
    flag=True
    for _ in range(n):
        numbers.append(input().strip())
    numbers.sort()
    for i in range(1,n):
        if len(numbers[i-1])>len(numbers[i]):
            continue
        if numbers[i-1]==numbers[i][:len(numbers[i-1])]:
            print("NO")
            flag=False
            break
    if flag:
        print("YES")
    t-=1