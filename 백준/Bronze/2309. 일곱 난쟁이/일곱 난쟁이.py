nan = [int(input()) for _ in range(9)]
index1, index2 = 0, 0
nan.sort()

for i in range(9):
    for j in range(9):
        if sum(nan) - (nan[i] + nan[j]) == 100:
            index1 = i
            index2 = j
            
del(nan[index1])
del(nan[index2])
print('\n'.join(map(str, nan)))