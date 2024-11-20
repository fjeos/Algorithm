import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
weights = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

for length in range(3, N + 1):
    for left in range(N - length + 1):
        right = left + length - 1
        for mid in range(left + 1, right):
            energy = weights[left] * weights[right]
            energy += dp[left][mid] + dp[mid][right]
            dp[left][right] = max(dp[left][right], energy)
print(dp[0][N-1])