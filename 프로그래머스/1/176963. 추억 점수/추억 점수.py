def solution(name, yearning, photo):
    answer = []
    dic = defaultdict(int)
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for k in range(len(photo)):
        score = 0
        for j in range(len(photo[k])):
            score += dic[photo[k][j]]
        answer.append(score)
        
    return answer

from collections import defaultdict