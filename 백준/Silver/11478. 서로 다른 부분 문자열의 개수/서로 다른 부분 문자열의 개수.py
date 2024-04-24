S = input()
part = set()

for j in range(len(S)):
    for repeat in range(1, len(S) + 1):
        s = S[j:j+repeat]
        if s in part:
            continue
        part.add(s)

print(len(part))
