N = int(input())
if N == 1:
    print(1)
else:
    tmp = 0
    k = 1
    while N > 2 + tmp - 1:
        tmp += 6 * k
        k += 1
    print(k)