import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y, h):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > h:
            dfs(nx, ny, h)


def count_safe_areas(h):
    global visited
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h)
                count += 1

    return count


max_height = max(map(max, graph))
max_safe_area = 0

for h in range(max_height + 1):
    max_safe_area = max(max_safe_area, count_safe_areas(h))

print(max_safe_area)
