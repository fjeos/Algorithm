from collections import defaultdict

lists = [list(map(int, input().split())) for _ in range(3)]

dic = defaultdict(int)
for i in range(3):
    dic[lists[i][0]] += 1

for k in dic:
    if dic[k] == 1:
        print(k, end=' ')

dic = defaultdict(int)
for i in range(3):
    dic[lists[i][1]] += 1

for k in dic:
    if dic[k] == 1:
        print(k, end=' ')

