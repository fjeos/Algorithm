from collections import defaultdict
def solution(clothes):
    N = len(clothes)
    answer = 1
    cases = defaultdict(int)
    
    for i in range(N):
        cases[clothes[i][1]] += 1
    
    summation = 0
    for case in cases:
        cases[case] += 1
        answer *= cases[case]

    return answer-1