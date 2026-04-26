def solution(n):
    ans_set = set()
    for i in range(1, n + 1):
        if n % i == 0:
            ans_set.add((i, n // i))
    result = {tuple(sorted(t)) for t in ans_set}
    return  sum(sum(set(t)) for t in result)