def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext == "code":
        for element in data:
            if element[0] < val_ext:
                answer.append(element)
    if ext == "date":
        for element in data:
            if element[1] < val_ext:
                answer.append(element)
    elif ext == "maximum":
        for element in data:
            if element[2] < val_ext:
                answer.append(element)
    elif ext == "remain": 
        for element in data:
            if element[3] < val_ext:
                answer.append(element)

    if sort_by == "code":
        answer.sort(key = lambda x: x[0])
    elif sort_by == "date":
        answer.sort(key = lambda x: x[1])
    elif sort_by == "maximum":
        answer.sort(key = lambda x: x[2])
    elif sort_by == "remain": 
        answer.sort(key = lambda x: x[3])
    return answer