from itertools import permutations
import re
def solution(expression):
    permu = list(permutations(['+', '-', '*'], 3))
    oper_list = re.split(r'(\D)', expression)
    max_value = 0
    for perms in permu:
        temp_list = oper_list[:]
        for op in perms:
            stack = []
            while temp_list:
                val = temp_list.pop(0)
                if val == op:
                    prev = stack.pop()
                    nex = temp_list.pop(0)
                    if val == '+':
                        stack.append(str(int(prev) + int(nex)))
                    elif val == '-':
                        stack.append(str(int(prev) - int(nex)))
                    else:
                        stack.append(str(int(prev) * int(nex)))
                else:
                    stack.append(val)
            temp_list = stack
        max_value = max(abs(int(temp_list[0])), max_value)
    return max_value
