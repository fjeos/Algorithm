import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations
num_problems, least_level, max_level, diff_level = map(int, input().split())
levels = list(map(int, input().split()))
levels.sort()
answer = 0

for i in range(2, num_problems + 1):
    result = list(combinations(levels, i))
    for pairs in result:
        if least_level <= sum(pairs) <= max_level and max(pairs) - min(pairs) >= diff_level:
            answer += 1

print(answer)
