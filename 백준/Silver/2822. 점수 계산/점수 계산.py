score = [int(input()) for _ in range(8)]
result = 0
scr = score.copy()
scr.sort(reverse = True)
lists = []
for i in range(5):
    result += scr[i]
print(result)
for i in range(5):
    for j in range(8):
        if score[j] == scr[i]:
            lists.append(j+1)
print(' '.join(map(str, sorted(lists))))