import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for i in range(N):
    summ = A[i]
    if summ == M:
        count += 1
        continue
    for j in range(i+1, N):
        summ += A[j]
        if summ == M:
            count += 1
            break
        elif summ > M:
            break
print(count)