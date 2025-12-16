S = input()
jub = []

for i in range(len(S)):
    jub.append(S[i:])

print('\n'.join(map(str, sorted(jub))))