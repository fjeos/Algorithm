N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
count = 0
coins.sort(reverse = True)

while K:
    for coin in coins:
        tmp = K // coin
        if tmp != 0:
            count += tmp
            K %= coin
            break
        else:
            continue
print(count)