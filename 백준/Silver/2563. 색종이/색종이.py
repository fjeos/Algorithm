lists = [[0]*101 for _ in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            lists[i][j] = 1
result = 0
for i in lists:
    result += i.count(1)
print(result)