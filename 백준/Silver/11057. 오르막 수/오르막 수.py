import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0, 10, 55] + [0 for _ in range(N-2)]
arr = list(range(10, 0, -1))
for i in range(3, N + 1):
    summ, sub = 0, 0
    for j in range(10):
        temp = arr[j] % 10007
        arr[j] = (dp[i - 1] % 10007) - (sub % 10007)
        sub += temp % 10007
        summ += arr[j] % 10007
    dp[i] = summ

print(dp[N] % 10007)
