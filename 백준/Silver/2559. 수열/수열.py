import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
temps = list(map(int, input().split()))

now_sum = sum(temps[0:K])
start, end = 0, K
result = now_sum
while end < N:
    now_sum = now_sum - temps[start] + temps[end]
    result = max(result, now_sum)
    start += 1
    end += 1
print(result)
