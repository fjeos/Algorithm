import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = list(map(int, input().split()))

acc = [sum(nums[1:])]
answer = [0 for _ in range(N)]
for i in range(1, N):
    acc.append(acc[i - 1] - nums[i])

for i in range(N):
    acc[i] = acc[i] * nums[i]

answer[0] = acc[0]
for j in range(1, N):
    answer[j] = answer[j - 1] + acc[j]

print(answer[-1])