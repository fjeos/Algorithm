dp = [0, 1, 1]
for i in range(3, 46):
    dp.append(dp[i-2] + dp[i-1])
print(dp[int(input())])