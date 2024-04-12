import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))
dp = [numbers[0]]
for i in range(1, N):
    dp.append(max(dp[i-1] + numbers[i], numbers[i]))
print(max(dp))