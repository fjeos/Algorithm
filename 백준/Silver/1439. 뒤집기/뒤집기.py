string = input()
S, list0, list1 = [], [], []
index = 0

for i in range(len(string)):
    S.append(string[i])

for i in range(len(S)):
    if i == len(S)-1:
        if S[i] == '0':
            list0.append(S[i])
        else:
            list1.append(S[i])
    elif S[i] != S[i+1]:
        if S[i] == '0':
            list0.append(S[index:i+1])
            index = i+1
        else:
            list1.append(S[index:i+1])
            index = i+1

print(min(len(list0), len(list1)))