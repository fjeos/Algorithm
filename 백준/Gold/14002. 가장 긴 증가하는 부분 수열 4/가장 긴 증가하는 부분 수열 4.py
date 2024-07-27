import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))
dp = [1 for _ in range(N)]
result = []

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)

length = max(dp)
for k in range(N-1, -1, -1):
    if dp[k] == length:
        result.append(numbers[k])
        length -= 1

print(max(dp))
print(' '.join(map(str, reversed(result))))
