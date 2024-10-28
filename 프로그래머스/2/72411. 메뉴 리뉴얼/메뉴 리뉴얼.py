from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
        
    for num in course:
        dic = defaultdict(int)
        for order in orders:
            combi = list(combinations(sorted(list(order)), num))
            for el in combi:
                dic[el] += 1
        answer.extend("".join(map(str, key)) for key, value in dic.items() if max(dic.values()) == value and value > 1)

        
    return sorted(answer)