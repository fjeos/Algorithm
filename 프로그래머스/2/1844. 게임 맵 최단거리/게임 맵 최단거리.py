# def solution(maps):
#     answer = 0
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     result = 1e9
#     dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     visited[0][0] = True
#     def dfs(x, y, count):
#         nonlocal result
#         if x == n - 1 and y == m - 1:
#             result = min(result, count)
#             return
#         for dx, dy in dxy:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 dfs(nx, ny, count + 1)
#                 visited[nx][ny] = False
#     dfs(0, 0, 1)
#     return result if result != 1e9 else -1

from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0, 0, 1)])
    count = 0
    visited[0][0] = True
    while queue:
        x, y, count = queue.popleft()
        if x == n - 1 and y == m - 1:
            return count
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
                

    return -1