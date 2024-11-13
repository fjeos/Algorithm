import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = sorted(list(map(int, input().split())))
target = int(input())

start, end, answer = 0, N - 1, 0
while start < end:
    sum_value = nums[start] + nums[end]
    if sum_value < target:
        start += 1
    elif sum_value > target:
        end -= 1
    else:
        answer += 1
        start += 1

print(answer)