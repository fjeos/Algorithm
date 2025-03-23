import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N, M, L = map(int, input().split())

dic = defaultdict(int)
i = 1
dic[i] = 1
count = 0
while True:
    if dic[i] >= M:
        break
    count += 1
    if dic[i] % 2 != 0:
        i += L
    else:
        i -= L
    if i > N:
        i -= N
    elif i <= 0:
        i = N + i
    dic[i] += 1

print(count)