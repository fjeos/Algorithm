def solution(s):
    stack = []
    
    for i in range(len(s)):
        if stack and s[i] == ')':
            stack.pop()
        else:
            stack.append('(')

    answer = (False if stack else True)
    return answer