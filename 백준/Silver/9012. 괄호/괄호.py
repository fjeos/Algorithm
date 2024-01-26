T = int(input())

for _ in range(T):
    stack = list(input())
    result = []
    isPVS = True
    for i in range(len(stack)):
        if stack[i] == "(":
            result.append(stack[i])
        elif stack[i] == ")":
            if not result:
                result.append(stack[i])
                continue
            elif result[0] != ")":
                result.pop()
    if result:
        print("NO")
    else:
        print("YES")
    