roll = list(0 for _ in range(0, int(input())+1))
maxi = 0
N = int(input())
for i in range(1, N+1):
    x, y = map(int, input().split())
    if y - x > maxi:
        maxi = y - x
        predi = i
    for j in range(x, y+1):
        if roll[j] != 0:
            continue;
        else:
            roll[j] = i
maxi = 0
for i in range(1, N+1):
    if maxi < roll.count(i):
        result = i
        maxi = roll.count(i)
print(predi)
print(result)