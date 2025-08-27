def solution(n):
    summ = [0]
    for i in range(1, n + 1):
        summ.append(summ[i-1] + i)
    left, right = 0, 1
    answer = 0
    while left < right:
        if summ[right] - summ[left] < n:
            right += 1
        else :
            if summ[right] - summ[left] == n:
                answer += 1
            left += 1
    return answer