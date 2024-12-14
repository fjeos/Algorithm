def solution(data, col, row_begin, row_end):
    answer = 0
    S = []
    data.sort(key=lambda x: (x[col-1], -x[0]))
    for i in range(row_begin-1, row_end):
        summ = 0
        for j in range(len(data[i])):
            summ += (data[i][j]%(i+1))
        S.append(summ)
    for s in S:
        answer ^= s
    return answer