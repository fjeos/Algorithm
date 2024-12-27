import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
dolls = list(map(int, input().split()))
result = []

start, end = 0, 0
lion = 0
while end < N:
    if lion < K:
        if dolls[end] == 1:
            lion += 1
        end += 1
    if lion == K:
        while dolls[start] == 2:
            start += 1
        result.append(end - start)
        start += 1
        lion -= 1
print(min(result) if result else -1)