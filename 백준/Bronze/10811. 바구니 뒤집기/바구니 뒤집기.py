N, M = map(int, input().split())
bask = []
for i in range(N):
    bask.append(i+1)
    
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    while i < j:
        temp = bask[i]
        bask[i] = bask[j]
        bask[j] = temp
        i += 1
        j -= 1
    
print(' '.join(map(str, bask)))