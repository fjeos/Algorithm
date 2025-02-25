import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

floor, start, goal, up, down = map(int, input().split())
result = []
queue = deque([(start, 0)])
visited = set()
visited.add(start)
while queue:
    now_floor, count = queue.popleft()
    if now_floor == goal:
        print(count)
        exit(0)
    go_up = now_floor + up
    if go_up <= floor and go_up not in visited:
        visited.add(go_up)
        queue.append((go_up, count + 1))
    go_down = now_floor - down
    if go_down >= 1 and go_down not in visited:
        visited.add(go_down)
        queue.append((go_down, count + 1))
print("use the stairs")
