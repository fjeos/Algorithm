result = 0

N, B = input().split()
B = int(B)
dic = {}
for i in range(10):
    dic[chr(48 + i)] = i
for i in range(10, 36):
    dic[chr(55 + i)] = i

j = len(N)-1
for i in range(len(N)):
    result += (dic[N[i]] * pow(B, j))
    j -= 1
print(result)