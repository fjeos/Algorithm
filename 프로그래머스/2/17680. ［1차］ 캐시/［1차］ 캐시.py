from collections import defaultdict
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    count = 0
    dic = defaultdict(int)
    
    for city in cities:
        city = city.lower()
        dic = {k: v + 1 for k, v in dic.items()}
        if city not in dic:
            if len(dic) == cacheSize:
                if dic:
                    max_value = max(dic.values())
                    result = next(k for k, v in dic.items() if v == max_value)
                    del dic[result]
                    dic[city] = 1
            count += 5
        else:
            count += 1
        dic[city] = 1
        
    return count
        