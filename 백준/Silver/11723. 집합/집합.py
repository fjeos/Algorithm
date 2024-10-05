import sys
input = lambda: sys.stdin.readline().rstrip()

S = set()
gen_list = set(range(1, 21))
for _ in range(int(input())):
    commands = input()
    if 'all' not in commands and 'empty' not in commands:
        command, num = commands.split()
        num = int(num)
    else:
        command = commands
    if command == 'add':
        S.add(num)
    elif command == 'remove':
        S.discard(num)
    elif command == 'check':
        print(1 if num in S else 0)
    elif command == 'toggle':
        S.discard(num) if num in S else S.add(num)
    elif command == 'all':
        S = gen_list.copy()
    else:
        S.clear()
