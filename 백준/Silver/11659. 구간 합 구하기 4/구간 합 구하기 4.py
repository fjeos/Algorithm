import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.insert(0, 0)

summation = [0]
for i in range(1, N + 1):
    summation.append(numbers[i] + summation[i-1])

for _ in range(M):
    start, end = map(int, input().split())
    print(summation[end] - summation[start - 1])
