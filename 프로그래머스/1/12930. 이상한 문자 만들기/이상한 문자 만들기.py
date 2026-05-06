def solution(s):
    answer = ''
    j = 0
    for i in range(len(s)):
        if s[i] != ' ':
            if j % 2 != 0:
                answer += s[i].lower()
            else:
                answer += s[i].upper()
            j += 1
        else:
            answer += s[i]
            j = 0
    
    return answer