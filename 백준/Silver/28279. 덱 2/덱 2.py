from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

deque = deque()
for _ in range(int(input())):
    command = input().split()
    if command[0] == '1':
        deque.appendleft(command[1])
    elif command[0] == '2':
        deque.append(command[1])
    elif command[0] == '3':
        print(deque.popleft() if deque else -1)
    elif command[0] == '4':
        print(deque.pop() if deque else -1)
    elif command[0] == '5':
        print(len(deque))
    elif command[0] == '6':
        print(0 if deque else 1)
    elif command[0] == '7':
        print(deque[0] if deque else -1)
    else:
        print(deque[-1] if deque else -1)
