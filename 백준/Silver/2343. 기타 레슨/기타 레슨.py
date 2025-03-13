import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
minutes = list(map(int, input().split()))
start, end = max(minutes), sum(minutes)
answer = sys.maxsize
while start <= end:
    mid = (start + end) // 2
    summ, i, disks = 0, 0, 1
    while i < N:
        summ += minutes[i]
        if summ > mid:
            disks += 1
            summ = 0
            if minutes[i] > mid:
                i += 1
            continue
        i += 1
    if disks > M:
        start = mid + 1
        continue
    answer = min(answer, mid)
    if disks <= M:
        end = mid - 1
    else:
        start = mid + 1

print(answer)
