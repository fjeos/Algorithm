def solution(new_id):
    symbol = "~!@#$%^&*()=+[{]}:?,<>/"
    temp = []
    answer = list(new_id.lower())
    index = 0
    while index < len(answer):
        if answer[index] in symbol:
            answer.pop(index)
            continue
        index += 1
    count, index, i, first = 0, 0, 0, False
    while i < len(answer):
        if answer[i] == '.':
            if first:
                first = False
                index = i
            count += 1
        else:
            if count > 0:
                temp.append(answer[index])
                i -= 1
            else:
                temp.append(answer[i])
                first = True
            count = 0
        i += 1
    new_id = ''.join(temp)
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')
    if not new_id:
        new_id += "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    if len(new_id) < 3:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id