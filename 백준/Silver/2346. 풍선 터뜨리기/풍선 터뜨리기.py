from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
balloons = deque(list(map(int, input().split())))
visited = [True, True] + [False] * (N - 1)
i = 1
answer = [1]
while not all(visited):
    repeat = balloons[i-1]
    if repeat < 0:
        while repeat < 0:
            i -= 1
            if i > N:
                i = 0
            elif i < 1:
                i = N
            if visited[i]:
                repeat -= 1
            repeat += 1
    else:
        while repeat > 0:
            i += 1
            if i > N:
                i = 0
            elif i < 1:
                i = N
            if visited[i]:
                repeat += 1
            repeat -= 1
    visited[i] = True
    answer.append(i)
print(' '.join(map(str, answer)))
