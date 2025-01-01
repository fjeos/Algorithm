N = int(input())
numbers = [list(str(k)) for k in range(1, N+1)]
if N < 100:
    count = N
else:
    count = 99
for i in range(100, N):
    if int(numbers[i][0]) - int(numbers[i][1]) == int(numbers[i][1]) - int(numbers[i][2]):
        count += 1
print(count)