import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

def min_value(i):
    mini = dp[i - 1][0]
    index = i-1
    if dp[i // 3][0] < mini:
        mini = dp[i//3][0]
        index = i//3
    if dp[i//2][0] < mini:
        mini = dp[i//2][0]
        index = i//2
    return index




if N == 1:
    print(0)
    print(1)
else:
    dp = [(0, 0), (0, 1), (1, 1), (1, 1)]
    for i in range(4, N+1):
        origin = 0
        if i % 6 == 0:
            origin = min_value(i)
        elif i % 2 == 0:
            origin = i//2 if dp[i//2][0] < dp[i-1][0] else i-1
        elif i % 3 == 0:
            origin = i//3 if dp[i//3][0] < dp[i-1][0] else i-1
        else:
            origin = i-1
        dp.append((dp[origin][0] + 1, origin))
    
    print(dp[N][0])
    index = N
    print(N, end=" ")
    while True:
        print(dp[index][1], end=" ")
        if dp[index][1] == 1:
            break
        index = dp[index][1]
