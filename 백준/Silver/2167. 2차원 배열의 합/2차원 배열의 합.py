import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
while K > 0:
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    answer = 0
    for nx in range(i, x + 1):
        for ny in range(j, y + 1):
            # print(nx, ny)
            answer += matrix[nx][ny]
    print(answer)
    K -= 1
