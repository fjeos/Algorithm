import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
directions = [input().split() for _ in range(L)]
board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for x, y in apples:
    board[x][y] = 1
now_direction = "R"  # R, L, U, D
i, now_sec = 0, 0
snake = defaultdict(int)
tail = deque([(1, 1)])
snake[(1, 1)] = 1
x, y = 1, 1
while True:
    if i < L:
        next_sec, turn = int(directions[i][0]), directions[i][1]
    while (i < L and now_sec != next_sec) or (i == L and now_sec >= next_sec):
        if now_direction == "R":
            y += 1
        elif now_direction == "L":
            y -= 1
        elif now_direction == "U":
            x -= 1
        elif now_direction == "D":
            x += 1
        if y == 0 or y == N + 1 or x == 0 or x == N + 1 or ((x, y) in snake.keys()):
            print(now_sec + 1)
            exit(0)
        elif board[x][y] == 0:
            tail_x, tail_y = tail.popleft()
            del snake[(tail_x, tail_y)]
        elif board[x][y] == 1:
            board[x][y] = 0
        snake[(x, y)] = 1
        tail.append((x, y))
        now_sec += 1
    if now_direction == "R":
        now_direction = "U" if turn == "L" else "D"
    elif now_direction == "L":
        now_direction = "D" if turn == "L" else "U"
    elif now_direction == "U":
        now_direction = "L" if turn == "L" else "R"
    elif now_direction == "D":
        now_direction = "R" if turn == "L" else "L"
    if i < L:
        i += 1
