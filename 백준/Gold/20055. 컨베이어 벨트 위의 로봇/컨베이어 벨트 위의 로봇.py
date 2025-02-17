import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robots = deque([False] * N)
stage, count = 0, 0
while count < K:
    stage += 1
    A.rotate(1)
    robots.rotate(1)
    robots[N - 1] = False
    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and A[i + 1] > 0:
            robots[i], robots[i + 1] = False, True
            A[i + 1] -= 1
            if A[i + 1] == 0:
                count += 1
    robots[N - 1] = False
    if A[0] > 0:
        robots[0] = True
        A[0] -= 1
        if A[0] == 0:
            count += 1

print(stage)
