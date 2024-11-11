from collections import deque
def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    queue = deque()
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0 ,0]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and not visited[i][j]:
                queue.append((i, j, maps[i][j]))
                count = 0
                visited[i][j] = True
                while queue:
                    x, y, day = queue.popleft()
                    count += int(day)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X" and not visited[nx][ny]:
                            queue.append((nx, ny, maps[nx][ny]))
                            visited[nx][ny] = True
                answer.append(count)
                
    if not answer:
        answer.append(-1)
    
    return sorted(answer)