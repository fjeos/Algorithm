from itertools import permutations


def calcResult(index, lists, operator):
    x, y = int(lists[index - 1]), int(lists[index + 1])
    lists.pop(index - 1)
    lists.pop(index - 1)
    lists.pop(index - 1)
    if operator == '*':
        result = x * y
    elif operator == '+':
        result = x + y
    else:
        result = x - y
    lists.insert(index - 1, result)


def solution(expression):
    answer, kinds, origin = [], set(), []
    temp = ''
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '*' or expression[i] == '-':
            kinds.add(expression[i])
            origin.append(temp)
            origin.append(expression[i])
            temp = ''
        else:
            temp += expression[i]
    origin.append(temp)
    perm = list(permutations(kinds, len(kinds)))

    for i in range(len(perm)):
        lists = origin[:]
        for j in range(len(perm[i])):
            if perm[i][j] == '*':
                try:
                    index = lists.index('*')
                    while index > 0:
                        calcResult(index, lists, '*')
                        index = lists.index('*')
                except ValueError:
                    continue
            elif perm[i][j] == '+':
                try:
                    index = lists.index('+')
                    while index > 0:
                        calcResult(index, lists, '+')
                        index = lists.index('+')
                except ValueError:
                    continue
            else:
                try:
                    index = lists.index('-')
                    while index > 0:
                        calcResult(index, lists, '-')
                        index = lists.index('-')
                except ValueError:
                    continue
        answer.append(abs(int(lists[0])))

    return max(answer)