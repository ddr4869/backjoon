from collections import deque

def solution(cacheSize1, cities):

    cities=[city.lower() for city in cities ]   

    cities_len=len(cities)
    if cacheSize1==0:
        return cities_len*5
    cache=deque()

    answer,cache_len=0,0
    for city in cities:

        if cache_len<cacheSize1 and city not in cache:
            cache_len+=1
            cache.append(city)
            answer+=5
        else:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer+=1
            else:
                cache.popleft()
                cache.append(city)
                answer+=5

    return answer