def solution(n):
    answer = pow(n, 0.5)
    return pow(answer+1, 2) if answer == int(answer) else -1
    