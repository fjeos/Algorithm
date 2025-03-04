import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(map(int, input().split()))
dic = defaultdict(int)
start, end = 0, 1
answer = 0
dic[nums[start]] = 1
while end < N:
    dic[nums[end]] += 1
    answer = max(answer, end - start)
    while dic[nums[end]] > K:
        dic[nums[start]] -= 1
        start += 1
    end += 1
print(max(answer, end - start) if start != 0 else N)
