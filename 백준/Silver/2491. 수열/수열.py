import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
dp_up = [1 for _ in range(N)]
dp_down = [1 for _ in range(N)]
for i in range(1, N):
    if nums[i - 1] <= nums[i]:
        dp_up[i] = dp_up[i - 1] + 1

for i in range(1, N):
    if nums[i - 1] >= nums[i]:
        dp_down[i] = dp_down[i - 1] + 1

print(max(max(dp_up), max(dp_down)))
