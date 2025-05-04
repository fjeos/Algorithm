numbers = [i for i in range(246913)]
numbers[1] = 0
for i in range(2, 246913):
    if numbers[i] != 0:
        for j in range(2*i, 246913, i):
            if numbers[j] != 0:
                numbers[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
                    
    for k in range(n + 1, 2 * n + 1):
        if numbers[k] != 0:
            count += 1
            
    print(count)