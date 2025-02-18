def back_tracking(depth, n):
    global answer
    if depth == n:
        answer += 1
        return
    
    for i in range(n):
        if i in col_set or (depth + i) in pos_diag_set or (depth - i) in neg_diag_set:
            continue

        col_set.add(i)
        pos_diag_set.add(depth + i)
        neg_diag_set.add(depth - i)

        back_tracking(depth + 1, n)

        col_set.remove(i)
        pos_diag_set.remove(depth + i)
        neg_diag_set.remove(depth - i)


def solution(n):
    global answer, col_set, pos_diag_set, neg_diag_set
    answer = 0
    col_set = set()
    pos_diag_set = set()
    neg_diag_set = set()
    back_tracking(0, n)
    return answer

