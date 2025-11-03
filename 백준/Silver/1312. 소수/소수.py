from decimal import Decimal
A, B, N = map(int, input().split())
lists = []

i, answer = 0, 0
K = A%B
while True:
    if K != 0:
        K *= 10
        lists.append(K//B)
        i += 1
        if i == N:
            answer = lists[-1]
            break
        K %= B
    else:
        if len(lists) < N:
            answer = 0
        else:
            answer = lists[N-1]
        break

print(answer)