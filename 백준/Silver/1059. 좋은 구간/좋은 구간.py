import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations

L = int(input())
nums = sorted(list(map(int, input().split())))
n = int(input())

if n < nums[0]:
        combi = list(combinations(range(1, nums[0]), 2))
else:
    index = 0
    for i in range(L - 1):
        if nums[i] < n < nums[i + 1]:
            index = i
            break
        if n < nums[0]:
            start = 1
            end = n + 1

    combi = list(combinations(range(nums[index] + 1, nums[index + 1]), 2))

answer = 0
for el in combi:
    if el[0] <= n <= el[1]:
        answer += 1
print(answer)
