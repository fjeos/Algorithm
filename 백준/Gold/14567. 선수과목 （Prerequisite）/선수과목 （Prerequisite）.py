import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n + 1)
for i in range(1, n + 1):
    visited[i] = True
    for el in graph[i]:
        result[el] = max(result[i] + 1, result[el])
        visited[el] = True

print(" ".join(map(str, result[1:])))
