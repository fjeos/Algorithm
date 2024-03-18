def solution(s, skip, index):
    answer = ''
    alphabet = []
    for i in range(26):
        alphabet.append(chr(i + 97))
    
    for j in range(len(s)):
        replace_index = alphabet.index(s[j])
        repeat = 0
        while repeat < index:
            replace_index += 1
            if replace_index > 25:
                replace_index = 0
            if alphabet[replace_index] in skip:
                repeat -= 1
            repeat += 1
            
        answer += alphabet[replace_index]
        
    return answer