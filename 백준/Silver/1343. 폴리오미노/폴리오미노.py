import sys

input = lambda: sys.stdin.readline().rstrip()

s = input()
s_copy = s.split('.')
answer = []
for el in s_copy:
    length = len(el)
    result = ''
    if length % 2 != 0:
        result = -1
    else:
        while length > 0:
            if length >= 4:
                result += 'AAAA'
                length -= 4
            elif length >= 2:
                result += 'BB'
                length -= 2
    answer.append(result)

print('.'.join(map(str, answer)) if -1 not in answer else -1)
