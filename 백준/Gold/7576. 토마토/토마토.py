from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
matured = deque()
for i in range(M):
    for j in range(N):
        if tomatoes[i][j] == 1:
            visited[i][j] = True
            matured.append((j, i))

if not any(0 in tomato for tomato in tomatoes):
    print(0)
else:
    days = 0
    queue = deque()
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while matured:
        while matured:
            queue.append(matured.popleft())
        while queue:
            x, y = queue.popleft()

            for n in range(4):
                nx = x + dx[n]
                ny = y + dy[n]
                if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and tomatoes[ny][nx] != -1:
                    matured.append((nx, ny))
                    tomatoes[ny][nx] = 1
                    visited[ny][nx] = True
        if matured:
            days += 1

    for k in range(M):
        if 0 in tomatoes[k]:
            days = -1
    print(days)
