from math import sqrt

N = int(input())
count = 0
for i in range(1, int(sqrt(N)) + 1):
    if i * i <= N:
        count += 1
print(count)
