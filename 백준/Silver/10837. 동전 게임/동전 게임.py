import sys

input = sys.stdin.readline

K = int(input())

for _ in range(int(input())):
    M, N = map(int, input().split())
    if M == N:
        answer = 1
    elif M < N:
        answer = 1 if (N - M) - (K - N) <= 1 else 0
    else:
        answer = 1 if (M - N) - (K - M) <= 2 else 0

    print(answer)
