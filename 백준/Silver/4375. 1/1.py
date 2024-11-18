while True:
    try:
        N = input()
    except Exception:
        break
    else:
        N = int(N)
    num, i = 1, 1
    while True:
        if num % N == 0:
            break
        else:
            i += 1
            num = num * 10 + 1
            num %= N
    print(i)