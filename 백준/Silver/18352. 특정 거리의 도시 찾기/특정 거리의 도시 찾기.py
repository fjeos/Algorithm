from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M, K, X = map(int, input().split())
maps = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    maps[u].append(v)

queue = deque([X])
visited = [-1] * (N + 1)
visited[X] = 0
result = []

while queue:
    current_city = queue.popleft()

    for next_city in maps[current_city]:
        if visited[next_city] == -1:  
            visited[next_city] = visited[current_city] + 1
            queue.append(next_city)

            if visited[next_city] == K:
                result.append(next_city)

if not result:
    print(-1)
else:
    for city in sorted(result):
        print(city)
