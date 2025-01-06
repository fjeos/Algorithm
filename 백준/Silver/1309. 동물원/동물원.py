import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0, 3, 7]
for i in range(3, N + 1):
    dp.append((dp[i - 1] * 2 + dp[i - 2]) % 9901)
print(dp[N])
