def solution(cacheSize, cities):
    answer = 0
    N = len(cities)
    for i in range(N):
        cities[i] = cities[i].lower()
    cache = {}
    
    if cacheSize == 0:
        answer = 5 * N
    else:
        for i in range(N):
            city = cities[i]
            if city in cache:
                answer += 1
                cache[city] = i
            else:
                if 0 < len(cache) >= cacheSize:
                    del(cache[min(cache, key = cache.get)])
                    cache[city] = i
                else:
                    cache[city] = i
                answer += 5
                
    return answer