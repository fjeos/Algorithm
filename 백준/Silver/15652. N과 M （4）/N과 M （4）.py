import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
result = []

def dp():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        result.append(i)
        if len(result) >= 2 and result[-1] < result[-2]:
            result.pop()
            continue
        dp()
        result.pop()


dp()
