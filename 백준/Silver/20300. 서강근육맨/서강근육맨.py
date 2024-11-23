import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
gym = sorted(list(map(int, input().split())))

result = 0
if N == 1:
    result = gym[0]
# 짝수
elif N % 2 == 0:
    for i in range(N // 2):
        result = max(gym[i] + gym[-i-1], result)
# 홀수
else:
    for i in range(N // 2):
        result = max(gym[i] + gym[-i-2], result)

print(result)
