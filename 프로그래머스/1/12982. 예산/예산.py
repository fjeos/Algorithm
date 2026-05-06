def solution(d, budget):
    answer, i = 0, 0
    length = len(d)
    d.sort()
    i = 0
    while i < length and budget >= d[i]:
        answer += 1
        budget -= d[i]
        i += 1
    return answer