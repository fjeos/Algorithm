import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

M, N, K = map(int, input().split())
road = [['O' for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range((y2-y1)):
        for x in range((x2-x1)):
            road[y1+y][x1+x] = 'X'

result = []
queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(M):
    for j in range(N):
        if road[i][j] != 'X':
            queue.append((i, j))
            count = 1
            while queue:
                y, x = queue.popleft()
                road[y][x] = 'X'
                for s in range(4):
                    nx = x + dx[s]
                    ny = y + dy[s]
                    if 0 <= nx < N and 0 <= ny < M and road[ny][nx] != 'X':
                        queue.append((ny, nx))
                        road[ny][nx] = 'X'
                        count += 1
            if count != 0:
                result.append(count)

print(len(result))
print(' '.join(map(str, sorted(result))))
