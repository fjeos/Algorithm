from collections import deque
def solution(N, road, K):
    maps = [{} for _ in range(N + 1)]
    dist = [K + 1] * (N + 1)
    dist[1] = 0
    success = {1}

    for a, b, c in road:
        if b not in maps[a] or maps[a][b] > c:
            maps[a][b] = c
            maps[b][a] = c

    queue = deque([1])

    while queue:
        a = queue.popleft()
        for b, c in maps[a].items():
            if dist[b] > c + dist[a]:
                dist[b] = dist[a] + c
                queue.append(b)
                success.add(b)

    return len(success)