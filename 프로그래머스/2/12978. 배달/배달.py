import heapq
def solution(N, road, K):
    graph = [[] for i in range(N + 1)]
    for info in road:
        graph[info[0]].append([info[1], info[2]])
        graph[info[1]].append([info[0], info[2]])
    dp = [1e9] * (N + 1)
    dp[1] = 0
    heap = []
    heapq.heappush(heap, (1, 0))
    while heap:
        curr_node, curr_dist = heapq.heappop(heap)
        if curr_dist <= dp[curr_node]:
            for node, dist in graph[curr_node]:
                next_dist = curr_dist + dist
                if next_dist < dp[node]:
                    dp[node] = next_dist
                    heapq.heappush(heap, (node, next_dist))
    
    return len([i for i in dp if i <= K])