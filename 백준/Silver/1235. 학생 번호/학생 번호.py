N = int(input())
students = [input() for _ in range(N)]
lists = ["" for _ in range(N)]
isDup = True

M = len(students[0])
for j in range(M-1, -1, -1):
    for i in range(N):
        lists[i] += students[i][j]
    if len(lists) == len(set(lists)):
        break
         
print(len(lists[i]))