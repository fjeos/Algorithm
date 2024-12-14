import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, P = map(int, input().split())
fingers = [deque() for _ in range(7)]
count = 0

for _ in range(N):
    n_row, n_prat = map(int, input().split())

    # 현재 줄의 현재 프랫보다 큰 프랫 삭제
    while fingers[n_row] and fingers[n_row][0] > n_prat:
        fingers[n_row].popleft()
        count += 1

    # 현재 줄을 누르고 있지 않거나 누르고 있는 프랫이 현재 프랫보다 작을 때
    if not fingers[n_row] or fingers[n_row][0] < n_prat:
        fingers[n_row].appendleft(n_prat)
        count += 1

print(count)
