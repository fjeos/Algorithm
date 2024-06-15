import sys
input = lambda: sys.stdin.readline().rstrip()

global count1
count1 = 0

def fib(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    count2 = 1
    f = [0] * n
    f[1] = f[2] = 1
    for i in range(3, n):
        f[i] = f[i - 1] + f[i - 2]
        count2 += 1
    return count2


n = int(input())
fib(n)
print(count1, fibonacci(n))
