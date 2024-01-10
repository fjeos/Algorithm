arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))
    
arrMax = max(map(max, arr))
print(arrMax)
#arr = list(arr)
for i in range(9):
    for j in range(9):
        if arr[i][j] == arrMax:
            print(i+1, j+1)
            break