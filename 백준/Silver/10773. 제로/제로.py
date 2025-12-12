result = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        del(result[len(result)-1])
    else:
        result.append(n)
print(sum(result))