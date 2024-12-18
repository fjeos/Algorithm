import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    step = list(range(10, 0, -1))
    dp = [0, 10, 55]
    for i in range(3, n+1):
        temp = dp[i-1]
        for k in range(10):
            numbers = step[k]
            step[k] = temp
            temp -= numbers
        step[0] = dp[i-1]
        dp.append(sum(step))

    print(dp[n])