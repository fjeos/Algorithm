H, M = map(int, input().split())
if M - 45 < 0:
    if H == 0:
        H = 23
    else:
        H -= 1
    print(H, 60 + (M - 45))
else:
    print(H, M - 45)