import re, sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == '.':
        break
    stack = []
    balance = False
    s = re.sub(r'[^()\[\]]', '', s)
    if not s:
        balance = True
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')' or s[i] == ']':
            if stack:
                symbol = stack.pop()
                if s[i] == ')' and symbol == '(':
                    balance = True
                elif s[i] == ']' and symbol == '[':
                    balance = True
                else:
                    balance = False
                    break
            else:
                balance = False
                break
    if stack:
        balance = False
    if balance:
        print("yes")
    else:
        print("no")