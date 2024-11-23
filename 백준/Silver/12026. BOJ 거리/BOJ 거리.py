import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
road = input()
dp = [1e9] * N
dp[0] = 0
for i in range(1, N):
    for j in range(i):
        if road[i] == 'B' and road[j] == 'J' or \
            road[i] == 'O' and road[j] == 'B' or \
            road[i] == 'J' and road[j] == 'O':
                dp[i] = min(dp[i], (j - i) ** 2 + dp[j])

print(dp[N - 1] if dp[N-1] != 1e9 else -1)
