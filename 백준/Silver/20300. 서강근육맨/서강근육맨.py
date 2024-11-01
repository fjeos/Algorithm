import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
PT = list(map(int, input().split()))
PT.sort()

if N % 2 == 0:
    result, end = 0, N - 1
else:
    result, end = PT[-1], N - 2

start = 0
while start < end:
    result = max(result, PT[start] + PT[end])
    start += 1
    end -= 1

print(result)
