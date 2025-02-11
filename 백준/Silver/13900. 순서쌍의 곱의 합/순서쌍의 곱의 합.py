import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))
total = sum(numbers)
answer = 0
for i in range(N):
    total -= numbers[i]
    answer += total * numbers[i]
print(answer)
