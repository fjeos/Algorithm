X = int(input())
mo, ja = [], []
temp, i = 0, 0
while True:
    temp += i
    if temp >= X:
        break
    i += 1
for j in range(1, i+1):
    ja.append(j)
mo = list(reversed(ja))
if ja[-1] % 2 == 0:
    print("{0}/{1}".format(mo[temp-X], ja[temp-X]))
else:
    print("{0}/{1}".format(ja[temp-X], mo[temp-X]))