import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
queue = []
for i in range(N):
    if A[i] == 0:
        queue.append(B[i])
result = []

for i in range(M):
    if queue:
        result.append(queue.pop())

for j in range(M - len(result)):
    result.append(C[j])

print(' '.join(map(str, result)))
