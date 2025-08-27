from collections import deque
def solution(s):

    queue = deque()
    for i in s:
        if queue and queue[-1] == i:
            queue.pop()
        else:
            queue.append(i)
    
    return 0 if queue else 1