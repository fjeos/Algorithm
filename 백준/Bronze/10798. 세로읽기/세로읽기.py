arr = []
maxlen = 0
for i in range(5):
    arr.append(input())
    if len(arr[i]) > maxlen:
        maxlen = len(arr[i])
for i in range(maxlen):
    for j in range(5):
        if len(arr[j]) <= i:
            continue
        print(arr[j][i], end='')