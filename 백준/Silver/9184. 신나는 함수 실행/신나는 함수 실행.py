import sys

input = lambda: sys.stdin.readline().rstrip()

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                dp[i][j][k] = 1
            elif i < j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = 1")
    elif a > 20 or b > 20 or c > 20:
        print(f"w({a}, {b}, {c}) = {dp[20][20][20]}")
    else:
        print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")
