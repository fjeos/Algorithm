N = int(input())
def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
if isPrime(N) and N != 1:
    print(N)
elif N != 1:
    j = 2
    while N > 1:
        if N % j == 0:
            print(j)
            N //= j
        else:
            j += 1