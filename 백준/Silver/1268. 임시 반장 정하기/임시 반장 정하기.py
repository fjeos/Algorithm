N = int(input())
classs = [input().split() for _ in range(N)]
same = [0]*N
for i in range(N):
    same[i] = [0]*N
for i in range(5):
    for j in range(N):
        for k in range(j+1, N):
            if classs[j][i] == classs[k][i]:
                same[k][j] = 1
                same[j][k] = 1
count = []
for i in same:
    count.append(i.count(1))
    
print(count.index(max(count)) + 1)