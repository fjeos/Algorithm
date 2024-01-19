lists = list(map(int, input().split()))
result = 0
for i in range(len(lists)):
    result += (lists[i] ** 2)
print(result%10)