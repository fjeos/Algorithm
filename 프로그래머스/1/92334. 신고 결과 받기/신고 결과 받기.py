def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    dic = defaultdict(list)
    
    for i in range(len(report)):
        user_id, rep_id = report[i].split()
        if user_id not in dic[rep_id]:
            dic[rep_id].append(user_id)
    
    for rep in dic:
        lists = dic[rep]
        if len(lists) >= k:
            for element in lists:
                answer[id_list.index(element)] += 1
    
    return answer

from collections import defaultdict