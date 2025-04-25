import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
weights, values = [], []

for _ in range(N):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(K + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[N][K])

