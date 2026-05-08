def solution(t, p):
    answer = 0
    i, length = 0, len(p)
    comp = int(p)
    while i + length - 1 < len(t):
        if int(t[i:i+length]) <= comp:
            answer += 1
        i += 1
    return answer