dic = {}
count = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x not in dic:
        dic[x] = y
    else:
        if dic[x] != y:
            count += 1
            dic[x] = y
print(count)