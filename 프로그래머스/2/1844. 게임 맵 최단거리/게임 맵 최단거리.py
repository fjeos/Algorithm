from collections import deque
def solution(maps):
    answer = 1e9
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    queue = deque([(0, 0, 0)])
    visited[0][0] = True
    while queue:
        x, y, count = queue.popleft()
        count += 1
        if x == n - 1 and y == m - 1:
            return count
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny, count))
                visited[nx][ny] = True
    
    return -1