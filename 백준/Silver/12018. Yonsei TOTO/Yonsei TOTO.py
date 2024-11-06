import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

result = []
answer = 0
for _ in range(n):
    apply, limit = map(int, input().split())
    miles = sorted(list(map(int, input().split())), reverse=True)

    if apply >= limit:
        result.append(miles[limit - 1])
    else:
        result.append(1)
    result.sort()

for el in result:
    if m >= el:
        m -= el
        answer += 1
    else:
        break
print(answer)

