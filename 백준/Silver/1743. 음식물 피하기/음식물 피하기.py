import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
roads = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    roads[r-1][c-1] = 1

queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
for i in range(N):
    for j in range(M):
        if roads[i][j] == 1:
            queue.append((i, j))
            roads[i][j] = 0
            count = 0
            while queue:
                x, y = queue.popleft()
                count += 1
                for s in range(4):
                    nx = x + dx[s]
                    ny = y + dy[s]
                    if 0 <= nx < N and 0 <= ny < M and roads[nx][ny] == 1:
                        queue.append((nx, ny))
                        roads[nx][ny] = 0
            result.append(count)
print(max(result))
