class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        answer = 0

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    visited[x][y] = True
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                answer += 1
        return answer