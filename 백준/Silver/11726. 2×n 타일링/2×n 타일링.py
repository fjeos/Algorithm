N = int(input())
dp = [1, 2, 3]
for i in range(3, N):
    dp.append(dp[i - 2] + dp[i - 1])
print(dp[N - 1] % 10007)