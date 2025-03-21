import sys

input = lambda: sys.stdin.readline().rstrip()

A = input()
B = input()
longer, shorter = '', ''
long, short = 0, 0
if len(A) >= len(B):
    long, short = len(A) + 1, len(B) + 1
    longer, shorter = A, B
else:
    long, short = len(B) + 1, len(A) + 1
    longer, shorter = B, A

dp = [[0 for _ in range(short)] for _ in range(long)]

for i in range(1, long):
    for j in range(1, short):
        if longer[i - 1] == shorter[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(map(max, dp)))
