import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
prefix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        prefix[i+1][j+1] = board[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
max_sum = -1e9
for k in range(1, N + 1):
    for x in range(1, N - k + 2):
        for y in range(1, N - k + 2):
            x2 = x + k - 1
            y2 = y + k - 1
            total = prefix[x2][y2] - prefix[x - 1][y2] - prefix[x2][y - 1] + prefix[x - 1][y - 1]
            max_sum = max(max_sum, total)

print(max_sum)
