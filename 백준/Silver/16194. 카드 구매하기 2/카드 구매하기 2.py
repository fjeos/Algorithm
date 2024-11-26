import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 1e9)
dp = [1e9] * (N + 1)
dp[0], dp[1] = 0, cards[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + cards[j])

print(dp[N])
