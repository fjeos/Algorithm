import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(N, S, M, V):
    dp = [[False for _ in range(M+1)] for _ in range(N+1)]
    dp[0][S] = True
    for i in range(N):
        for j in range(M+1):
            if dp[i][j]:
                plus, minus = j + V[i], j - V[i]
                if plus <= M:
                    dp[i+1][plus] = True
                if minus >= 0:
                    dp[i+1][minus] = True

    max_value = -1
    for j in range(M+1):
        if dp[N][j]:
            max_value = max(max_value, j)
    print(max_value)


N, S, M = map(int, input().split())
V = list(map(int, input().split()))
solution(N, S, M, V)
