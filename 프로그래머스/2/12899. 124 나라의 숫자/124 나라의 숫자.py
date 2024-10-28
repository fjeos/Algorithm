from collections import deque
def solution(n):
    answer = deque()
    while n > 3:
        result = n % 3
        if n % 3 == 0:
            n = (n // 3) - 1
        else:
            n //= 3
        answer.appendleft(result if result != 0 else 4)
    answer.appendleft(n if n != 3 else 4)
    return ''.join(map(str, answer))