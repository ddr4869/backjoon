n = int(input())
roads = [0]+list(map(int, input().split()))
cities = list(map(int, input().split()))

lowPrice=cities[0]
distance=0
answer=0

for idx, cityPrice in enumerate(cities):
    if idx==0:
        continue
    distance=roads[idx]
    answer+=lowPrice*distance
    if cityPrice<lowPrice:
        lowPrice=cityPrice
print(answer)