from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

R, C, K = map(int, input().split())
road = [list(input()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
answer = 0


def dfs(x, y, dist):
    global answer
    if x == 0 and y == C - 1 and dist == K:
        answer += 1
    else:
        road[x][y] = 'T'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and road[nx][ny] != 'T':
                road[nx][ny] = 'T'
                dfs(nx, ny, dist + 1)
                road[nx][ny] = '.'


dfs(R - 1, 0, 1)
print(answer)
