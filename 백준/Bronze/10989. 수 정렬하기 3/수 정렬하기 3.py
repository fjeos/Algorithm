import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
counting = [0] * 10001

for _ in range(N):
    counting[int(input())] += 1

for i in range(10001):
    while counting[i] > 0:
        print(i)
        counting[i] -= 1
