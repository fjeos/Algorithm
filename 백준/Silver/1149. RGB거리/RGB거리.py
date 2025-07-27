import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(3)]
dp[0][0] = RGB[0][0]
dp[1][0] = RGB[0][1]
dp[2][0] = RGB[0][2]

for i in range(1, N):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + RGB[i][0]
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + RGB[i][1]
    dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + RGB[i][2]

print(min(dp[0][N-1], dp[1][N-1], dp[2][N-1]))