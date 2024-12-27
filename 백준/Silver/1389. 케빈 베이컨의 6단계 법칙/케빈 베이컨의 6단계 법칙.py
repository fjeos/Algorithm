from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dp = [[1e9 for _ in range(N+1)] for _ in range(N+1)]
for s in range(1, N+1):
    dp[s][s] = 0
result = []
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    dp[A][B] = dp[B][A] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+ 1):
            dp[j][k] = min(dp[j][k], dp[j][i]+dp[i][k])

for s in dp:
    result.append(sum(s[1:]))
print(result.index(min(result)))
