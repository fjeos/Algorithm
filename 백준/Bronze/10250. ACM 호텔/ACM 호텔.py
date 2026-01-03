for _ in range(int(input())):
    H, W, N = map(int, input().split())
    fl, num = 0, 1
    if N > H:
        while N > H:
            N -= H
            num += 1
    fl += N
    fl *= 100
    print(fl + num)