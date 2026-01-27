N = int(input())
list1 = []
list2 = []
i = 1
for _ in range(1, N + 1):
    list1.append(i)
    i += 1

while len(list1) != 1:
    list2.append(list1[0])
    del(list1[0])
    list1.append(list1[0])
    del(list1[0])
    
list2.append(list1[0])
print(' '.join(map(str, list2)))