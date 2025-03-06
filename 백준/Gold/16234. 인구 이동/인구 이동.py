import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
days = 0
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
to_check = set((i, j) for i in range(N) for j in range(N))


def bfs(i, j, visited):
    queue = deque([(i, j)])
    union = [(i, j)]
    visited[i][j] = True
    sum_people = maps[i][j]

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(maps[x][y] - maps[nx][ny]) <= R:
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    sum_people += maps[nx][ny]
                    visited[nx][ny] = True
    if len(union) > 1: 
        new_people = sum_people // len(union)
        for x, y in union:
            maps[x][y] = new_people
        new_check.update(union)
        for x, y in union:
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    new_check.add((nx, ny))
        return True
    return False

while to_check:
    visited = [[False] * N for _ in range(N)]
    new_check = set()
    moved = False
    for i, j in list(to_check):
        if not visited[i][j]:
            if bfs(i, j, visited):
                moved = True
    if not moved:
        break 
    to_check = new_check
    days += 1

print(days)
