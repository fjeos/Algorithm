import re
def solution(s):
    answer = []
    dic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9}
    
    temp = ''
    for i in s:
        if not re.match('[0-9]', i):
            temp += i
        else:
            answer.append(i)
        if temp in dic:
            answer.append(dic[temp])
            temp = ''
    return int(''.join(map(str, answer)))