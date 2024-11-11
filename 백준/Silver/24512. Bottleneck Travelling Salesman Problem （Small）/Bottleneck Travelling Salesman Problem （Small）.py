import sys
input = lambda: sys.stdin.readline().rstrip()

def DFS(now, count, cost):
    global max_cost
    global result
    if count == N:
        if graph[now][start] == 0:
            return
        cost = max(cost, graph[now][start])

        if cost < max_cost:
            max_cost = cost
            result = routes[:]

    for j in range(1, N+1):
        if graph[now][j] == 0 or visited[j]:
            continue
        visited[j] = True
        routes[count] = j
        DFS(j, count + 1, max(cost, graph[now][j]))
        visited[j] = False


N, M = map(int, input().split())
graph = [[1e9 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N + 1)]
result = []
routes = [0 for _ in range(N)]
start, max_cost = 0, 1e9
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u][v] = c

for i in range(1, N+1):
    visited[i] = True
    routes[0] = i
    start = i
    DFS(i, 1 ,0)
    visited[i] = False

if max_cost == 1e9:
    print(-1)
    exit(0)
print(max_cost)
for el in result:
    print(el, end=" ")
