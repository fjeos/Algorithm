from collections import deque

def bfs(now_x, now_y, rooms):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((now_x, now_y))
    visited = [[False]*5 for _ in range(5)]
    visited[now_x][now_y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                dist = abs(nx - now_x) + abs(ny - now_y)
                if dist <= 2 and rooms[nx][ny] == 'P':
                    return False
                elif dist < 2 and rooms[nx][ny] == 'O':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return True

def solution(places):
    answer = []
    
    for place in places:
        is_False = False
        for j in range(5):
            for p in range(5):
                if place[j][p] == 'P':
                    if not bfs(j, p, place):
                        is_False = True
                        break
            if is_False:
                break
        answer.append(1 if not is_False else 0)
                    
                    
    return answer