import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
team = [False for _ in range(N)]
result = 1e9


def recur(index, count):
    if count == N // 2:
        min_value()
        return
    for i in range(index, N):
        if not team[i]:
            team[i] = True
            recur(i, count + 1)
            team[i] = False


def min_value():
    global result
    start, link = 0, 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if team[i] and team[j]:
                start += stat[i][j]
                start += stat[j][i]
            elif not team[i] and not team[j]:
                link += stat[i][j]
                link += stat[j][i]
    diff = abs(start - link)
    if diff == 0:
        print(diff)
        exit(0)
    result = min(result, diff)


recur(0, 0)
print(result)