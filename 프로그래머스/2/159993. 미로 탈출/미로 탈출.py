from collections import deque
def solution(maps):
    w, h = len(maps[0]), len(maps)
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    start = False
    queue = deque()
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                queue.append((i, j, 0))
                start = True
                visited[i][j] = True
                break
        if start:
            break

    # 1번 : S -> L 최단 거리
    lx, ly = 0, 0
    while queue:
        y, x, count = queue.popleft()
        if maps[y][x] == 'L':
            answer = count
            lx, ly = x, y
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] != 'X' and not visited[ny][nx]:
                queue.append((ny, nx, count + 1))
                visited[ny][nx] = True

    if answer == 0: 
        return -1

    # 2번 : L -> E 최단 거리
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append((ly, lx, 0))
    while queue:
        y, x, count = queue.popleft()
        if maps[y][x] == 'E':
            return answer + count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] != 'X' and not visited[ny][nx]:
                queue.append((ny, nx, count + 1))
                visited[ny][nx] = True

    return -1