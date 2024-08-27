import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stones = list(map(int, input().split()))
dp = [1e9 for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    min_value = -1
    for j in range(i):
        K = (i - j) * (1 + abs(stones[i] - stones[j]))
        dp[i] = min(dp[i], max(dp[j], K))

print(dp[N - 1])

