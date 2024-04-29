import math, sys
input = lambda: sys.stdin.readline().rstrip()


def is_prime(x: int) -> bool:
    if x == 0 or x == 1:
        return False
    for j in range(2, int(math.sqrt(x) + 1)):
        if x % j == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    if is_prime(n):
        print(n)
    else:
        n += 1
        while not is_prime(n):
            n += 1
        print(n)
        