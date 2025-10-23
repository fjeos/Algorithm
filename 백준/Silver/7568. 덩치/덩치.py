N = int(input())
dung = []
result = [0 for _ in range(N)]
for _ in range(N):
    dung.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i+1, N):
        if dung[i][0] > dung[j][0] and dung[i][1] > dung[j][1]:
            result[j] += 1
        elif dung[i][0] < dung[j][0] and dung[i][1] < dung[j][1]:
            result[i] += 1
                
for i in range(N):
    print(result[i]+1, end = ' ')