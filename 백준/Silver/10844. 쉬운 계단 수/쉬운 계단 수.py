n = int(input())
result = [[0]*10 for _ in range(n+1)]

for i in range(1, 10):
    result[1][i] = 1
    
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            result[i][j] = result[i-1][1]
        elif j > 0 and j < 9:
            result[i][j] = result[i-1][j-1] + result[i-1][j+1]
        else:
            result[i][j] = result[i-1][j-1]

print(sum(result[n])%1000000000)