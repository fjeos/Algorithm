import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    answer = 0
    for i in range(n // 3 + 1):
        temp = n - (3 * i)
        answer += (temp // 2 + 1)
    print(answer)
