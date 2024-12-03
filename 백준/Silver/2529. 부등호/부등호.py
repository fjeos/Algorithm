import sys

input = lambda: sys.stdin.readline().rstrip()

k = int(input())
symbols = input().split()
visited = [False] * 10
min_value, max_value = "", ""


def check(left, symbol, right):
    return left > right if symbol == '>' else left < right


def dfs(num, depth):
    global min_value, max_value
    if depth == k + 1:
        if len(min_value) == 0:
            min_value = num
        else:
            max_value = num
        return

    for i in range(10):
        if not visited[i] and (depth == 0 or check(num[-1], symbols[depth - 1], str(i))):
            visited[i] = True
            dfs(num+str(i), depth + 1)
            visited[i] = False

dfs("", 0)
print(max_value)
print(min_value)