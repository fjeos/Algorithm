apt = [[0]*15 for _ in range(15)]
for i in range(1, 15):
    apt[0][i] = i
    
for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, j+1):
            apt[i][j] += apt[i-1][k]
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(apt[k][n])