import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    dic[int(input())] += 1
max_value = max(dic.values())
print([key for key, value in sorted(dic.items()) if max_value == value][0])
