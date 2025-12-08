M, N = map(int, input().split())
numbers = [i for i in range(N + 1)]
numbers[1] = 0

for i in range(2, N + 1):
    if numbers[i] != 0:
        for j in range(2*i, N + 1, i):
            if numbers[j] != 0:
                numbers[j] = 0

print('\n'.join(list(map(str, filter(lambda x: x != 0, numbers[M:])))))