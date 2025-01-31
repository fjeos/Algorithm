import sys

input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
dic = dict()
for i in range(2, B+1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        dic[i] = 1

def soinsu_bunhae(N):
    factors = []
    for i in range(2, int(N ** 0.5) + 1):
        while N % i == 0:
            factors.append(i)
            N //= i

    if N > 1:
        factors.append(N)
    return len(factors)


answer = 0
for i in range(A, B + 1):
    if soinsu_bunhae(i) in dic.keys():
        answer += 1

print(answer)
