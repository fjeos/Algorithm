n = input()
num1 = list(map(int, n))
n = input()
num2 = list(map(int, n))
result = []
res = []

for i in range(8):
    result.append(num1[i])
    result.append(num2[i])
k = 0

for j in range(14):
    for i in range(15-(k)):
        result[i] = ((result[i] + result[i+1])%10)  
    k+=1

res.append(result[0])
res.append(result[1])
print(''.join(map(str, res)))