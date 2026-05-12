def solution(babbling):
    answer = 0
    invalid = ["ayaaya", "yeye", "woowoo", "mama"]
    for el in babbling:
        valid = True
        for word in invalid:
            if word in el:
                valid = False
                break
        if valid:
            i = 0
            length = len(el)
            possible = True
            while i < length:
                if i + 1 < length and i + 2 < length and \
                el[i] == 'a' and el[i+1] == 'y' and el[i+2] == 'a':
                    i += 3
                elif i + 1 < length and el[i] == 'y' and el[i+1] == 'e':
                    i += 2
                elif i + 1 < length and i + 2 < length and \
                el[i] == 'w' and el[i + 1] == 'o' and el[i+2] == 'o':
                    i += 3
                elif i + 1 < length and el[i] == 'm' and el[i+1] == 'a':
                    i += 2
                else:
                    possible = False
                    break
            if possible:
                answer += 1
    return answer