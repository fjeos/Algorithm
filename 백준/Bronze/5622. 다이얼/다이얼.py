s = list(input())
dic = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
sec = 0
for i in range(len(s)):
    for key, value in dic.items():
        if s[i] in value:
            sec += key + 1
print(sec)