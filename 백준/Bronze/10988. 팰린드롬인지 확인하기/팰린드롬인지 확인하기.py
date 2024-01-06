s = input()
isPal = False
length = len(s)//2

if len(s) == 1: isPal = True
for i in range(length):
    if s[i] != s[-i-1]:
        break
    elif i == length-1:
        isPal = True
        
print('1' if isPal else '0')    