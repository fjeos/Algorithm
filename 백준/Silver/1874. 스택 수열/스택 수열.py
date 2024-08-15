import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
numbers = [int(input()) for _ in range(n)]
stack, result = [1], ['+']
j = 2


for i in range(n):
    if numbers[i] >= j:
        stack.append(j)
        result.append("+")
        j += 1
    while stack[len(stack)-1] != numbers[i]:
        last = stack[len(stack) - 1]
        if numbers[i] > last:
            stack.append(j)
            result.append('+')
            j += 1
        elif numbers[i] != last and j > last + 1:
            break
        else:
            stack.pop()
            result.append('-')

    if stack[-1] == numbers[i]:
        stack.pop()
        result.append('-')

if stack:
    print("NO")
    exit(0)
print('\n'.join(result))
