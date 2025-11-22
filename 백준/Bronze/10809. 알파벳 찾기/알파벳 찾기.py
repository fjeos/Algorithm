al = [chr(i) for i in range(97, 123)]
s = input()
count = 0
for i in range(26):
    if al[i] in s:
        print(s.index(al[i]), end = '')
    else:
        print(-1, end = '')
    if i < 25:
        print(" ", end = '')