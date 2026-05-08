def solution(s, n):
    answer = ''
    for el in s:
        if el == " ":
            answer += " "
        else:
            if el.islower():
                answer += chr((ord(el) - ord('a') + n) % 26 + ord('a'))
            else:
                answer += chr((ord(el) - ord('A') + n) % 26 + ord('A'))
    return answer