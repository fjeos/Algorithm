N, B = map(int, input().split())

dic = {key : chr(key + 55) for key in range(10, 36)}

s = []
while N > 0:
    remainder = N % B
    if remainder in dic:
        s.insert(0, dic[remainder])
    else:
        s.insert(0, str(remainder))
    N = int(N / B)

print(''.join(s))