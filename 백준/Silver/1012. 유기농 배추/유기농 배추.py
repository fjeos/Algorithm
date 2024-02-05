from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
    result = []
    worm = 0
    
    queue = deque()
    for k in range(N):
        for l in range(M):
            if field[k][l] == 0 or visited[k][l]:
                continue
            queue.append((k, l))
            while queue:
                x, y = queue.popleft()
                visited[x][y] = True
                
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            worm += 1
            
    print(worm)