import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
    if n > 1:
        dp[0][1], dp[1][1] = dp[1][0] + stickers[0][1], dp[0][0] + stickers[1][1]
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))
