import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(int(input())):
    N = int(input())
    now_x, now_y = map(int, input().split())
    move_x, move_y = map(int, input().split())
    queue = deque()
    queue.append((now_x, now_y, 0))
    result = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    least_path = 99999
    while queue:
        x, y, count = queue.popleft()
        if x == move_x and y == move_y:
            result.append(count)
            least_path = min(result)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and count <= least_path:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True
    print(min(result))
