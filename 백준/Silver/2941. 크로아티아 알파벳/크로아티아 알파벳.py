string = list(input())
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = []
i = 0
count = 0
while i < len(string) - 2:
    if string[i] == 'c' and string[i+1] == '=':
        count += 1
        i += 2
    elif string[i] == 'c' and string[i+1] == '-':
        count += 1
        i += 2
    elif string[i] == 'd' and string[i+1] == 'z' and string[i+2] == '=':
        count += 1
        i += 3
    elif string[i] == 'd' and string[i+1] == '-':
        count += 1
        i += 2
    elif string[i] == 'l' and string[i+1] == 'j':
        count += 1
        i += 2
    elif string[i] == 'n' and string[i+1] == 'j':
        count += 1
        i += 2
    elif string[i] == 's' and string[i+1] == '=':
        count += 1
        i += 2
    elif string[i] == 'z' and string[i+1] == '=':
        count += 1
        i += 2
    else:
        count += 1
        i += 1
        

while i < len(string) - 1:
    if string[i] == 'c' and string[i+1] == '=':
        count += 1
        i += 2
    elif string[i] == 'c' and string[i+1] == '-':
        count += 1
        i += 2
    elif string[i] == 'd' and string[i+1] == '-':
        count += 1
        i += 2
    elif string[i] == 'l' and string[i+1] == 'j':
        count += 1
        i += 2
    elif string[i] == 'n' and string[i+1] == 'j':
        count += 1
        i += 2
    elif string[i] == 's' and string[i+1] == '=':
        count += 1
        i += 2
    elif string[i] == 'z' and string[i+1] == '=':
        count += 1
        i += 2
    else:
        count += 1
        i += 1

if i == len(string):
    print(count)
else:
    print(count+1)