from itertools import combinations
from collections import defaultdict
def solution(relation):
    answer = 0
    dic = defaultdict(int)
    row, col = len(relation), len(relation[0])
    combi = []
    for i in range(col):
        combi.extend(list(combinations(range(col), i)))
    combi.pop(0)
    result = []
    
    for case in combi:
        is_possible = True
        if len(set(tuple([data[i] for i in case]) for data in relation)) == row:
            now_case = set(case)
            if not result:
                answer += 1
                result.append(now_case)
            for item in result:
                if item.issubset(now_case):
                    is_possible = False
            if is_possible:
                answer += 1
                result.append(now_case)
    return answer if answer != 0 else 1