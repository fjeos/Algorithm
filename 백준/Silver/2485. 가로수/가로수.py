import sys
from math import gcd
input = lambda: sys.stdin.readline().rstrip()

position = [int(input()) for _ in range(int(input()))]
diff = [position[i+1] - position[i] for i in range(len(position)-1)]
distance = gcd(*diff)
result = 0
for num in diff:
    result += (num//distance)-1
print(result)