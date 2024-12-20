from collections import deque
def solution(board):
    row = len(board[0])
    col = len(board)
    queue = deque()
    visited = [[1e9 for _ in range(row)] for _ in range(col)]
    for i in range(col):
        for j in range(row):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                visited[i][j] = 0
                break
        if queue:
            break
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        y, x, count = queue.popleft()
        if board[y][x] == 'G':
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < row and 0 <= ny < col and board[ny][nx] != 'D':
                nx += dx[i]
                ny += dy[i]
            nx -= dx[i]
            ny -= dy[i]
            if visited[ny][nx] > count + 1:
                visited[ny][nx] = count + 1
                queue.append((ny, nx, count + 1))
        
    return -1