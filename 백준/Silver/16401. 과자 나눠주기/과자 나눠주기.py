import sys
input = lambda: sys.stdin.readline().rstrip()

nephs, sticks = map(int, input().split())
snacks = list(map(int, input().split()))
answer = 0

start, end = 1, max(snacks)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for snack in snacks:
        if snack >= mid:
            count += (snack // mid)
    if count < nephs:
        end = mid - 1
    else:
        start = mid + 1
        answer = max(answer, mid)
print(answer)