import sys

input = lambda: sys.stdin.readline().rstrip()

nums = input()
result = []

# 최댓값
number = ''
count_M = 0
for i in range(len(nums)):
    if nums[i] == 'M':
        count_M += 1
    else:
        if count_M > 0:
            number += '5' + ('0' * count_M)
            count_M = 0
        else:
            number += '5'
if count_M > 0:
    number += '1' * count_M
print(number)

# 최솟값
number = ''
count_M = 0
for i in range(len(nums)):
    if nums[i] == 'M':
        count_M += 1
    else:
        if count_M > 0:
            number += '1' + ('0' * (count_M - 1)) + '5'
        else:
            number += '5'
        count_M = 0
if count_M > 0:
    number += '1' + ('0' * (count_M - 1))
print(number)
