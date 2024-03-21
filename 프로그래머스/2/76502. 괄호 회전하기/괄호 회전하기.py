def solution(s):
    answer = 0
    n = len(s)
    string = list(s)
    for _ in range(n):        
        stack = []
        for i in range(n):
            symbol = string[i]
            if symbol == '(' or symbol == '{' or symbol == '[':
                stack.append(symbol)
                
            elif stack and ((symbol == ')' and stack[-1] == '(') or 
            (symbol == '}' and stack[-1] == '{') or
            (symbol == ']' and stack[-1] == '[')):
                stack.pop()
                
            else:
                stack.append(symbol)
        if not stack:
            answer += 1
        
        string.append(string.pop(0))
    return answer