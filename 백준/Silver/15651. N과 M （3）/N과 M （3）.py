import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
result = []
visited = [False] * (N + 1)

def dp():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        result.append(i)
        visited[i] = True
        dp()
        result.pop()
        visited[i] = False
dp()