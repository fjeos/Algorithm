N = list(map(int, input()))

length = len(N)
for i in range(length-1):
    for j in range(i+1, length):
        if N[i] < N[j]:
            temp = N[i]
            N[i] = N[j]
            N[j] = temp
print(''.join(map(str, N)))