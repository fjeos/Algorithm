import sys, re
input = lambda: sys.stdin.readline().rstrip()

lines = [input() for _ in range(int(input()))]

exp = r'[a-z]'
result = []
for line in lines:
    split_list = re.split(exp, line)
    for el in split_list:
        if el != '':
            result.append(int(el))

print('\n'.join(map(str, sorted(result))))
