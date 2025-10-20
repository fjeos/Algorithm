N = int(input())
words = [input() for _ in range(N)]
count = 0
for i in range(N):
    dic = {}
    dic[words[i][0]] = 1
    for j in range(1, len(words[i])):     
        if words[i][j-1] == words[i][j]:
            continue;
        elif words[i][j] in dic:
            dic[words[i][j]] = 0
        else:
            dic[words[i][j]] = 1
    if 0 not in dic.values():
        count += 1
print(count)