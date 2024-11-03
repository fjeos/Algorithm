import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations
num_problems, least_level, max_level, diff_level = map(int, input().split())
levels = sorted(list(map(int, input().split())))

answer = 0

for i in range(2, num_problems + 1):
    for pairs in combinations(levels, i):
        if least_level <= sum(pairs) <= max_level and pairs[-1] - pairs[0] >= diff_level:
            answer += 1

print(answer)
