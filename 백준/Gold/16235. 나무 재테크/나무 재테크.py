import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
bat = [[5] * N for _ in range(N)]
graph = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x - 1][y - 1].append(z)

for x in range(N):
    for y in range(N):
        graph[x][y] = deque(sorted(graph[x][y]))

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]

while K > 0:
    breeding_trees = []
    # spring, summer
    for x in range(N):
        for y in range(N):
            if not graph[x][y]:
                continue
            new_trees = deque()
            dead_nutrients = 0

            while graph[x][y]:
                age = graph[x][y].popleft()
                if bat[x][y] >= age:
                    bat[x][y] -= age
                    new_trees.append(age + 1)
                    if (age + 1) % 5 == 0:
                        breeding_trees.append((x, y))
                else:
                    dead_nutrients += age // 2

            bat[x][y] += dead_nutrients
            graph[x][y] = new_trees 

    # autumn
    for x, y in breeding_trees:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                graph[nx][ny].appendleft(1) 

    # winter
    for x in range(N):
        for y in range(N):
            bat[x][y] += A[x][y]

    K -= 1


count = sum(len(graph[x][y]) for x in range(N) for y in range(N))
print(count)
