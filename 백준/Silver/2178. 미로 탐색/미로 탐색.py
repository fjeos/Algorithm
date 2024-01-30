from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, str(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
queue.append((0,0))
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    if miro[x][y] == 0:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N :
            if 0 <= ny < M and not visited[nx][ny] and miro[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                miro[nx][ny] = miro[x][y] + 1
                    
print(miro[N-1][M-1])