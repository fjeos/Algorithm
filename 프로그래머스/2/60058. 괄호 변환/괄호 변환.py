def check_right_string(string):
    stack = []
    for symbol in string:
        if symbol == '(':
            stack.append(symbol)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def divide(string):
    left_count, right_count = 0, 0
    for i in range(len(string)):
        if string[i] == '(':
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:
            return string[:i + 1], string[i + 1:]


def solution(p):
    if p == '':
        return p

    u, v = divide(p)

    if check_right_string(u):
        return u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        for s in u[1: len(u) - 1]:
            if s == '(':
                result += ')'
            else:
                result += '('
        return result
