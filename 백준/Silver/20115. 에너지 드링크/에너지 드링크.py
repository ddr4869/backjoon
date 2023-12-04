n = int(input())
drinks = list(map(int, input().split()))

drinks.sort()
answer=0
for volume in drinks[:-1]:
    answer+=volume/2

if (answer+drinks[-1]).is_integer():
    print(int(answer + drinks[-1]))
else:
    print(round(answer+drinks[-1],5))
