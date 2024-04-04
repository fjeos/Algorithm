def solution(priorities, location):
    answer = 0 
    prioDict = {} 
    
    for i, prio in enumerate(priorities):
        prioDict[i] = prio

    maxNum = max(prioDict.values())

    while priorities[location] != 0: 
        for i in prioDict:
            if prioDict[i] == maxNum:
                answer = answer + 1  
                if i == location:
                    return answer
                prioDict[i] = 0  
                maxNum = max(prioDict.values())