import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [1, 1]
for i in range(2, N):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[-1])