from collections import deque

N = int(input())
jido = [list(map(int, str(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
danji = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
for k in range(N):
    for l in range(N):
        if jido[k][l] == 0 or visited[k][l]:
            continue
        queue.append((k, l))
        count = 1
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and jido[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
        danji.append(count)

print(len(danji))
print('\n'.join(map(str, sorted(danji))))