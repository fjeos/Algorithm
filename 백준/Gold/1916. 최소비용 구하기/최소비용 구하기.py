import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

num_cities = int(input())
num_buses = int(input())
shortest_path = [1e9 for _ in range(num_cities + 1)]
graph = [[] for _ in range(num_cities + 1)]
for _ in range(num_buses):
    from_, to, cost = map(int, input().split())
    graph[from_].append([to, cost])
start, end = map(int, input().split())
queue = []
heapq.heappush(queue, (0, start))
shortest_path[start] = 0

while queue:
    distance, now_node = heapq.heappop(queue)
    if shortest_path[now_node] < distance: continue

    for next_node in graph[now_node]:
        cost = shortest_path[now_node] + next_node[1]
        if cost < shortest_path[next_node[0]]:
            shortest_path[next_node[0]] = cost
            heapq.heappush(queue, (cost, next_node[0]))

print(shortest_path[end])
