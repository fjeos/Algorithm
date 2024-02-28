import math
N = int(input())
count = 0
fact = str(math.factorial(N))
for i in range(len(fact)-1, 0, -1):
    if fact[i] == '0':
        count += 1
    else:
        break
print(count)