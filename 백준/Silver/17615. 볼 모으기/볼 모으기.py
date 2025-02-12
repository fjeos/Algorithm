import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
balls = input()
R_count = balls.count('R')
B_count = balls.count('B')
result = 1e9

# R을 왼쪽으로
count = 0
for i in range(N):
    if balls[i] == 'R':
        count += 1
    else:
        break
result = min(result, R_count - count)

# R을 오른쪽으로
count = 0
for i in range(N - 1, -1, -1):
    if balls[i] == 'R':
        count += 1
    else:
        break
result = min(result, R_count - count)

# B를 왼쪽으로
count = 0
for i in range(N):
    if balls[i] == 'B':
        count += 1
    else:
        break
result = min(result, B_count - count)

# B를 왼쪽으로
count = 0
for i in range(N - 1, -1, -1):
    if balls[i] == 'B':
        count += 1
    else:
        break
result = min(result, B_count - count)

print(result)