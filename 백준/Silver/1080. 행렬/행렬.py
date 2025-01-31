import sys

input = lambda: sys.stdin.readline().rstrip()


def reverse_list(x, y):
    for k in range(x, x + 3):
        for s in range(y, y + 3):
            if origin[k][s] == '0':
                origin[k][s] = origin[k][s].replace('0', '1')
            else:
                origin[k][s] = origin[k][s].replace('1', '0')


N, M = map(int, input().split())
origin = [list(input()) for _ in range(N)]
goal = [list(input()) for _ in range(N)]
if N < 3 and M < 3:
    print(0) if all(a == b for a, b in zip(origin, goal)) else print(-1)
else:
    count = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if origin[i][j] != goal[i][j]:
                reverse_list(i, j)
                count += 1

    if all(a == b for a, b in zip(origin, goal)):
        print(count)
    else:
        print(-1)