import sys

input = lambda: sys.stdin.readline().rstrip()

v6 = input()
comp = v6.split(":")
if '' in comp:
    index = comp.index('')
if len(comp) > 8:
    comp.pop(comp.index(''))
    
for i in range(len(comp)):
    length = len(comp[i])
    if length < 4:
        if length == 0:
            comp[i] = '0000'
        else:
            temp = '0' * (4 - length)
            comp[i] = temp + comp[i]

while len(comp) < 8:
    comp.insert(index, '0000')
print(":".join(comp))

