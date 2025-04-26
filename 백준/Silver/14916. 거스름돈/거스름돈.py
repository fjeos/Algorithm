n = int(input())

present = 0
count = 0

if n % 5 == 0:
    print(n // 5)
else:
    while n % 5 != 0:
        n -= 2
        count += 1
        if n < 0:
            count = -1
            break
    if n >= 0:
        count += n // 5
    print(count)