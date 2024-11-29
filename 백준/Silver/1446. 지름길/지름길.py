import sys

input = lambda: sys.stdin.readline().rstrip()

N, D = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]

dp = [1e9] * (D + 1)
dp[0] = 0
for i in range(1, D + 1):
    dp[i] = dp[i - 1] + 1
    for start, end, shortcut in roads:
        if i == end:
            dp[i] = min(dp[i], dp[start] + shortcut)
print(dp[D])
