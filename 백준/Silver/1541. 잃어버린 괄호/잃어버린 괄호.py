sik = input()
values = ['(']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
integer = ''
for i in range(len(sik)):
    if sik[i] in numbers:
        integer += sik[i]
    else:
        values.append(int(integer))
        integer = ''
        if sik[i] == '-':
            values.append(')-(')
        else:
            values.append('+')
values.append(int(integer))
values.append(')')
print(eval(''.join(map(str, values))))