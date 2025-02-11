import sys, heapq

input = lambda: sys.stdin.readline().rstrip()


def dijkstra(N, M):
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    dp = [1e9] * (N+1)
    dp[1] = 0
    heap = []
    heapq.heappush(heap, (1, 0))
    while heap:
        curr_node, curr_cost = heapq.heappop(heap)
        if curr_cost <= dp[curr_node]:
            for node, cost in graph[curr_node]:
                next_cost = curr_cost + cost
                if next_cost < dp[node]:
                    dp[node] = next_cost
                    heapq.heappush(heap, (node, next_cost))
    
    print(dp[N])


N, M = map(int, input().split())
dijkstra(N, M)
