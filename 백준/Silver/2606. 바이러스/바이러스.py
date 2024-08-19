import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N = int(input())
pairs = int(input())
computers = [[] for _ in range(N + 1)]
for i in range(pairs):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)
visited = [False for _ in range(N + 1)]
queue = deque(computers[1])
while queue:
    index = queue.popleft()
    for com in computers[index]:
        if not visited[com] and com != 1:
            queue.append(com)
            visited[com] = True
    visited[index] = True
print(visited.count(True))
