string = input()
n = len(string)
result = []    
for i in range(n-2):
    for j in range(i+1, n-1):
        list1, list2 = [], []
        list1.append(string[0:i+1])
        list1.append(string[i+1:j+1])
        list1.append(string[j+1:])
        for k in list1:
            list2.append(k[::-1])
        result.append(''.join(list2))
print(sorted(result)[0])