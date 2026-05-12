def solution(answers):
    answers.insert(0, 0)
    answer = []
    questions = len(answers)
    one, two, three = [0], [0] * (questions + 1), [0]
    count = 1
    for _ in range(questions):
        one.append(count)
        count += 1
        if count > 5:
            count = 1
    count = 1
    for i in range(1, questions + 1):
        if i % 2 == 0:
            two[i] = count
            if count == 1:
                count += 2
            else:
                count += 1
            if count > 5:
                count = 1
        else:
            two[i] = 2
    #print(two)
    count = 1
    while count <= questions:
        three.append(3)
        three.append(3)
        three.append(1)
        three.append(1)
        three.append(2)
        three.append(2)
        three.append(4)
        three.append(4)
        three.append(5)
        three.append(5)
        count += 10
    
    one_count, two_count, three_count = 0, 0, 0
    for j in range(1, questions):
        if answers[j] == one[j]:
            one_count += 1
        if answers[j] == two[j]:
            two_count += 1
        if answers[j] == three[j]:
            three_count += 1
    max_count = max(one_count, two_count, three_count)
    if one_count == max_count:
        answer.append(1)
    if two_count == max_count:
        answer.append(2)
    if three_count == max_count:
        answer.append(3)
    return answer