import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
bowls = [int(input()) for _ in range(N)]

start, end = 1, max(bowls)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(N):
        count += bowls[i] // mid
    if count >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)