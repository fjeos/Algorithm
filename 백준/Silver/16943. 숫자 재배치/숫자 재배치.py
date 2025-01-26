import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(A, B):
    digits = sorted(A)
    B = int(B)
    max_value = -1
    visited = [False] * len(A)

    def backtrack(current):
        nonlocal max_value
        if len(current) == len(digits):
            num = int("".join(current))
            if num > B:
                return
            max_value = max(max_value, num)

        for i in range(len(digits)):
            if (visited[i]) or (not current and digits[i] == '0'):
                continue
            visited[i] = True
            backtrack(current + [digits[i]])
            visited[i] = False

    backtrack([])
    return max_value


A, B = input().split()
print(solution(A, B))
