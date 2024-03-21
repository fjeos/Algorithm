def solution(s):
    answer = []
    lists = list(s.split("},{"))
    N = len(lists)
    for i in range(N):
        lists[i] = lists[i].strip("{""}")
    
    tup = []
    for i in range(N):
        tup.append(list(map(int, lists[i].split(","))))
    tup.sort(key = lambda x: len(x))
    
    for element in tup:
        for k in range(len(element)):
            if element[k] not in answer:
                answer.append(element[k])
    return answer