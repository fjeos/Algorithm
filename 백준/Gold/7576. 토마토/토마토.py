import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

matured = deque()

for col in range(N):
    for row in range(M):
        if tomato_box[col][row] == 1:
            matured.append((col, row))

while matured:
    col, row = matured.popleft()

    for n in range(4):
        n_row = row + dx[n]
        n_col = col + dy[n]
        if 0 <= n_row < M and 0 <= n_col < N and tomato_box[n_col][n_row] == 0:
            matured.append((n_col, n_row))
            tomato_box[n_col][n_row] = tomato_box[col][row] + 1


days = 0
for tomatoes in tomato_box:
    if 0 in tomatoes:
        print(-1)
        exit(0)
    else:
        days = max(days, max(tomatoes))
        
print(days - 1)
