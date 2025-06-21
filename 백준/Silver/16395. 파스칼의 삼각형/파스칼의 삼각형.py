pascal = [[1], [1, 1]]

n, k = map(int, input().split())
for i in range(2, n):
    pascal.append([])  
    for j in range(i+1):
        if j == 0 or j == i:
            pascal[i].insert(j, 1)
        else:
            pascal[i].insert(j, pascal[i-1][j-1] + pascal[i-1][j])
            
print(pascal[n-1][k-1])