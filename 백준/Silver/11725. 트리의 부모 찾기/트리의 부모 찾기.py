import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
result = [0 for _ in range(N + 1)]

queue = deque([[1, tree[1]]])
while queue:
    parent, nodes = queue.popleft()
    for i in range(len(nodes)):
        if nodes[i] == 1 or result[nodes[i]] != 0:
            continue
        result[nodes[i]] = parent
        queue.append([nodes[i], tree[nodes[i]]])

for i in range(2, N + 1):
    print(result[i])