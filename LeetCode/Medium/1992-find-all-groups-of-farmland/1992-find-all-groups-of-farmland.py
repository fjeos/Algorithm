class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        group = []
        queue = deque()
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]

        for i in range(m):
            for j in range(n):
                if land[i][j] <= 0:
                    continue
                queue.append((i, j))
                max_x, max_y = i, j
                while queue:
                    x, y = queue.popleft()
                    land[x][y] -= 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and land[nx][ny] == 1:
                            queue.append((nx, ny))
                            land[nx][ny] -= 1
                            if nx > max_x:
                                max_x = nx
                            if ny > max_y:
                                max_y = ny
                group.append([i, j, max_x, max_y])

        return group

