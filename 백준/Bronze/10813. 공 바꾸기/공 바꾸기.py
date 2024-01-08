N, M = map(int, input().split())

bask = []
for i in range(N):
    bask.append(str(i+1))

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    temp = bask[i]
    bask[i] = bask[j]
    bask[j] = temp

print(' '.join(bask))