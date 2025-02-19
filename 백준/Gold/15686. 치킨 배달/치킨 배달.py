import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize
stores, houses = [], []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            stores.append((i, j))


def cal_dist(chickens):
    result = 0
    for house_x, house_y in houses:
        this_min = sys.maxsize
        for chicken_x, chicken_y in chickens:
            this_min = min(this_min, abs(house_x - chicken_x) + abs(house_y - chicken_y))
        result += this_min
    return result


def dfs(depth, index, chickens):
    global min_value
    if depth == M:
        min_value = min(min_value, cal_dist(chickens))
        return

    for i in range(index, len(stores)):
        chickens.append(stores[i])
        dfs(depth + 1, i + 1, chickens)
        chickens.pop()


dfs(0, 0, [])
print(min_value)
