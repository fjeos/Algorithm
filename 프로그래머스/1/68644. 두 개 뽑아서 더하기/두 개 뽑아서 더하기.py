def solution(numbers):
    answer = set()
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            answer.add(numbers[i] + numbers[j])
    return sorted(list(answer))