N = int(input())
result = []
current = 0

for i in range(N):
    temp = [N, N-i]
    while True:
        current = temp[-2] - temp[-1]
        if current < 0:
            break
        temp.append(current)
    if len(temp) > len(result):
        result = temp.copy()
        
print(len(result))
print(' '.join(map(str, result)))