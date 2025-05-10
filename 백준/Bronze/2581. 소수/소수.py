M = int(input())
N = int(input())
numbers = list(range(M, N+1))
for i in range(M, N+1):
    if i == 1:
        del(numbers[numbers.index(i)])
        continue
    for j in range(2, i):
        if i % j == 0:
            del(numbers[numbers.index(i)])
            break
if len(numbers) > 0:
    print(sum(numbers))
    print(min(numbers))
else:
    print(-1)