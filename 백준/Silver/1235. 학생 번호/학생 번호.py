N = int(input())
stu = []

for _ in range(N):
    stu.append(input())
    
length = len(stu[0])

for i in range(1, length+1):
    result = []
    for j in range(N):
        if stu[j][-i:] in result:
            break
        else:
            result.append(stu[j][-i:])
    if len(result) == N:
        print(i)
        break