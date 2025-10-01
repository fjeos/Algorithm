string = input()
s, res = '', ''
seq = 0
for i in range(len(string)):
    if string[i].isupper():
        s += string[i]

for j in range(len(s)):
    if s[j] == 'U' and seq == 0:
        res += 'U'
        seq += 1
    elif s[j] == 'C' and seq == 1:
        res += 'C'
        seq += 1
    elif s[j] == 'P' and seq == 2:
        res += 'P'
        seq += 1
    elif s[j] == 'C' and seq == 3:
        res += 'C'
        seq += 1
        
if res == 'UCPC':
    print("I love UCPC")
else:
    print("I hate UCPC")