T = int(input())
coin = [25, 10 ,5, 1]

for _ in range(T):
    N = int(input())
    ret = [0, 0, 0, 0]
    for i in range(4):
        share = N // coin[i]
        ret[i] += share
        N %= coin[i]
        share = N
    print(' '.join(list(map(str, ret))))
        