import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
blocks = input()
dp = [1e9] * N
dp[0] = 0
for i in range(1, N):
    for j in range(i + 1):
        if blocks[i] == 'B' and blocks[j] == 'J':
            dp[i] = min(dp[i], dp[j] + abs(i - j) ** 2)
        elif blocks[i] == 'O' and blocks[j] == 'B':
            dp[i] = min(dp[i], dp[j] + abs(i - j) ** 2)
        elif blocks[i] == 'J' and blocks[j] == 'O':
            dp[i] = min(dp[i], dp[j] + abs(i - j) ** 2)
print(dp[N-1] if dp[N-1] != 1e9 else -1)
