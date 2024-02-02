N, M = map(int, input().split())

basket = []
for _ in range(N):
    basket.append(0)

for _ in range(M):
    i, j, k = map(int, input().split())
    for s in range(i-1, j):
        basket[s] = k
for s in range(N):
    if s < N-1:
        print(basket[s], end = ' ')
    else:
        print(basket[s], end = '')