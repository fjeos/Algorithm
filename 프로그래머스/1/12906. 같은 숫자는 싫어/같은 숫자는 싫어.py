from collections import deque
def solution(arr):
    answer = deque([arr[0]])
    
    for el in arr:
        if answer[-1] != el:
            answer.append(el)
    
    return list(answer)