import math
def solution(k, d):
    answer = 0
    dist = d ** 2
    for x in range(0, d + 1, k):
        if x > d:
            break
        answer += math.sqrt(dist - x **2) // k + 1
        
    return answer