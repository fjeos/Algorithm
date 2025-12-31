def d(n):
    tot = int(n)
    for i in range(len(n)):
        tot += int(n[i])
    return tot

numbers = set()
for j in range(1, 10001):
    numbers.add(d(str(j)))

for k in range(1, 10001):
    if k not in numbers:
        print(k)