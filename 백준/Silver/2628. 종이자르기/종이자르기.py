col, row = map(int, input().split())
N = int(input())
Rcut = [0]
Ccut = [0]
for i in range(N):
    x, y = map(int, input().split())
    if x == 0:
        Ccut.append(y)
    else:
        Rcut.append(y)
Ccut.append(row)
Rcut.append(col)
Ccut.sort()
Rcut.sort()

result = 0
for i in range(1, len(Ccut)):
    height = Ccut[i] - Ccut[i-1]
    for j in range(1, len(Rcut)):
        width = Rcut[j] - Rcut[j-1]
        result = max(result, width*height)
        
print(result)