import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
repeat = 1
while True:
    s = input()
    if s.count('-') > 0:
        break
    queue = deque()
    count = 0
    for i in range(len(s)):
        if s[i] == '{':
            queue.append(s[i])
        else:
            if queue:
                queue.popleft()
            else:
                count += 1
                queue.append('{')

    count = count + 1 if len(queue) == 1 else count + (len(queue)//2)
    print(f"{repeat}. {count}")
    repeat += 1

