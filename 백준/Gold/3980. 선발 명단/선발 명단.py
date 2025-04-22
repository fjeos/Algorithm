import sys

input = lambda: sys.stdin.readline().rstrip()


def dfs(depth, score):
    global answer
    if depth == 11:
        answer = max(score, answer)
    for position in range(11):
        if not visited[position] and board[depth][position] > 0:
            visited[position] = True
            dfs(depth + 1, score + board[depth][position])
            visited[position] = False


for _ in range(int(input())):
    board = [list(map(int, input().split())) for _ in range(11)]

    visited = [False] * 11
    answer = 0
    dfs(0, 0)
    print(answer)
