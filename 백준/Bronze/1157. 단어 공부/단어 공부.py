s = input()
s = s.upper()
dic = {}
for i in range(65, 91):
    dic[chr(i)] = 0
for i in range(len(s)):
    dic[s[i]] += 1
tmp = [k for k, v in dic.items() if max(dic.values()) == v]
if len(tmp) > 1:
    print("?")
else:
    print(tmp[0])