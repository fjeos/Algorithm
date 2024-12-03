import sys

input = lambda: sys.stdin.readline().rstrip()

factorial = [0, 1, 2]
for i in range(3, 1001):
    factorial.append(factorial[i - 1] * i)

while True:
    N = int(input())
    if N == 0:
        break
    print(factorial[2 * N] // (factorial[N] * factorial[N + 1]))
