def solution(s):
    answer = True
    p_count, y_count = 0, 0
    s = s.lower()
    for el in s:
        if el == 'p':
            p_count += 1
        elif el == 'y':
            y_count += 1
    return p_count == y_count