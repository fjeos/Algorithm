A = list(map(int, input()))
B = list(map(int, input()))
result = []

for i in range(2, -1, -1):
    temp = 0
    tmpList = []
    k = 0
    for j in range(2, 0, -1):
        tmpList.append((temp + (A[j] * B[i]) % 10) * (10 ** k))
        temp = (A[j] * B[i]) // 10
        k += 1
    j -= 1
    tmpList.append((temp + A[j] * B[i]) * 10 ** k)
    result.append(tmpList[0] + tmpList[1] + tmpList[2])
    
for i in range(3):
    print(result[i])
    result[i] *= (10 ** i)
print(result[0] + result[1] + result[2])