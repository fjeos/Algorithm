import sys
input = lambda: sys.stdin.readline().rstrip()

import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

N = int(input())
floats = [decimal.Decimal(input()) for _ in range(N)]
result = floats[0]

for i in range(N):
    mul = floats[i]
    result = max(result, mul)
    for j in range(i + 1, N):
        mul = decimal.Decimal(mul * floats[j])
        result = max(result, mul)

print("%.3f" % round(result, 3))
