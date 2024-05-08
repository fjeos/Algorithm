from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

queue = deque()
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0 if queue else 1)
    elif command[0] == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)