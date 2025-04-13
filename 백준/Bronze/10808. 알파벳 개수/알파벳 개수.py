s = input()
counts = [0 for _ in range(26)]
for i in range(26):
    counts[i] = s.count(chr(97 + i))
print(' '.join(map(str, counts)))