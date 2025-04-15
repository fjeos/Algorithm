N = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(N):
    if numbers[i] == 1:
        continue
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            count -= 1
            break
    count += 1
print(count)