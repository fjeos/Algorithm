import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
answer = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            queue.append((i, j))
            maps[i][j] = 0
            count = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                        maps[nx][ny] = 0
                        queue.append((nx, ny))
                        count += 1
            if count:
                answer.append(count)

print(len(answer))
print(max(answer) if answer else 0)
