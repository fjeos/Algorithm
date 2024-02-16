import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
results = []

for i in range(N):
    for k in range(K):
        temp = 0
        for j in range(M):
            temp += A[i][j]*B[j][k]
        results.append(temp)
        
count = 0
for i in range(len(results)):
    print(results[i], end = ' ')
    count += 1
    if count % K == 0:
        print()