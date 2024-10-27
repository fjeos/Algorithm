from collections import deque
N = int(input())
queue = deque(list(range(1, N + 1)))
stage = 1

while len(queue) > 1:
    miss = (stage ** 3) % len(queue)
    if miss != 1:
        queue.rotate(-(miss - 1))
    queue.popleft()
    stage += 1

print(queue[0])