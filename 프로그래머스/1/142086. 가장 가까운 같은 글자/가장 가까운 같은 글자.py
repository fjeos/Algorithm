def solution(s):
    answer = [0 for _ in range(len(s)) ]
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic.keys():
            dic[s[i]] = i
            answer[i] = -1
        else:
            answer[i] = i - dic[s[i]]
            dic[s[i]] = i
    return answer