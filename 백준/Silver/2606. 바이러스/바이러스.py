from collections import deque 

N = int(input()) 
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M): 
    u, v = map(int, input().split()) 
    graph[u] += [v]
    graph[v] += [u]

visited = [0] * (N+1)
visited[1] = 1

queue = deque([1])
while queue:
    v = queue.popleft()
    for nextCom in graph[v]:
        if visited[nextCom] == 0:
            queue.append(nextCom)
            visited[nextCom] = 1
    
print(sum(visited) - 1)