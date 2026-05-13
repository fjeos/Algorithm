def solution(s):
    answer = []
    
    for i, ch in enumerate(s):
        if i == 0 or s[i - 1] == ' ':
            answer.append(ch.upper())
        else:
            answer.append(ch.lower())
            
    return ''.join(answer)
