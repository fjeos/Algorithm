import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]

for i in range(N):
    queue = deque()
    queue.append(i)
    visited = [False] * N
    while queue:
        q = queue.popleft()
        for j in range(N):
            if not visited[j] and matrix[q][j] == 1:
                queue.append(j)
                visited[j] = True
                result[i][j] = 1

for el in result:
    print(*el)