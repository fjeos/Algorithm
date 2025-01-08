def solution(s):
    result = []
    for i in range(1, len(s)+1):
        count = 1
        answer = ''
        temp = s[:i]
        for j in range(i, len(s) + i, i):
            if s[j:j+i] == temp:
                count += 1
            else:
                if count != 1:
                    answer += str(count) + temp
                else:
                    answer += temp
                temp = s[j:j+i]
                count = 1
        result.append(len(answer))
    return min(result)