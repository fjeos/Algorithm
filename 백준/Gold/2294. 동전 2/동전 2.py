import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = list(set(int(input()) for _ in range(n)))
dp = [sys.maxsize for _ in range(k + 1)]
dp[0] = 0
for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != sys.maxsize:
            dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[k] if dp[k] != sys.maxsize else -1)