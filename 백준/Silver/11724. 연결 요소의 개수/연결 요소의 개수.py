from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
queue = deque()
count = 1
for _ in range(M):
    u, v = map(int, input().split())
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)
        
for i in range(1, N+1):
    if visited[i]:
        continue
    queue.append(i)
    while queue:
        x = queue.popleft()
        if not visited[x]:
            for j in range(len(graph[x])):
                queue.append(graph[x][j])
            visited[x] = True
    if not all(visited[1:]):
        count += 1
    else:
        break
print(count)