def solution(n, m, section):
    if m == 1:
        return len(section)
    answer = 0
    index = 0
    for el in section:
        if el > index:
            answer += 1
            index = el + m - 1
    return answer