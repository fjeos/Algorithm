def solution(s):
    answer = ''
    lists = list(map(int, s.split()))
    print(lists)
    answer = str(min(lists))
    answer += ' '
    answer += str(max(lists))
    return answer