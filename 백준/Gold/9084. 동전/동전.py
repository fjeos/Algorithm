import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    coins.insert(0, 0)
    goal = int(input())

    dp = [[0 for _ in range(goal + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1

    for i in range(1, N + 1):
        for j in range(1, goal + 1):
            dp[i][j] = dp[i - 1][j]
            if j - coins[i] >= 0:
                dp[i][j] += dp[i][j - coins[i]]
    print(dp[N][goal])
