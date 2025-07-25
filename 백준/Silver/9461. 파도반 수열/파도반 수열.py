import sys

input = lambda: sys.stdin.readline().rstrip()

dp = [0, 1, 1, 1]
for i in range(4, 101):
    dp.append(max(dp[i - 1], dp[i - 2] + dp[i - 3]))

for _ in range(int(input())):
    print(dp[int(input())])
