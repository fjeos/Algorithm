import math

n = int(input())
sqrt = math.isqrt(n)
print(sqrt + 1 if sqrt ** 2 != n else sqrt)