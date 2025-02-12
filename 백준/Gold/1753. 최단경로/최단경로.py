import sys, heapq

input = lambda: sys.stdin.readline().rstrip()


def solution(V, E, K):
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, c = map(int, input().split())
        graph[u].append([v, c])
    dist = [sys.maxsize] * (V + 1)
    dist[K] = 0
    
    heap = []
    heapq.heappush(heap, (0, K))
    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > dist[curr_node]:
            continue
        for node, cost in graph[curr_node]:
            next_dist = curr_dist + cost
            if next_dist < dist[node]:
                dist[node] = next_dist
                heapq.heappush(heap, (next_dist, node))

    for i in range(1, V + 1):
        print(dist[i] if dist[i] != sys.maxsize else "INF")


V, E = map(int, input().split())
K = int(input())
solution(V, E, K)
