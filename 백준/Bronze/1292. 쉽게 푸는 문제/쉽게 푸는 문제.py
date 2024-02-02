A, B = map(int, input().split())
lists = [0]
result = 0

for i in range(1, B+1):
    for j in range(1, i+1):
        lists.append(i)

for i in range(A, B+1):
    result += lists[i]
    
print(result)