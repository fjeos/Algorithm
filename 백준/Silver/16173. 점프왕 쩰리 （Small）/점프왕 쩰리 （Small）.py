from collections import deque
N = int(input())
jelly = [list(map(int, input().split())) for _ in range(N)]
printed = False
queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    temp = jelly[x][y]
    if temp == -1:
        print("HaruHaru")
        printed = True
    elif temp < N and temp > 0:
        if x + temp >= N and y + temp >= N:
            continue
        elif x + temp >= N :
            queue.append((x, y+temp))
        elif y + temp >= N:
            queue.append((x+temp, y))
        else:
            queue.append((x+temp, y))
            queue.append((x, y+temp))

if not printed:
    print("Hing")