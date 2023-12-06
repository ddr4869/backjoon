import sys
input = sys.stdin.readline

n = int(input())
cities=[]

for i in range(n):
    cities.append(tuple(map(int,input().split())))

cities.sort()
numberOfPeople=0
for i in range(n):
    numberOfPeople+=cities[i][1]
sum=0
for i in range(n):
    sum+=cities[i][1]
    if sum>=numberOfPeople/2:
        print(cities[i][0])
        break