def solution(n, k):
    answer = []

    factorial = [1, 1]
    for i in range(2, n + 1):
        factorial.append(factorial[i - 1] * i)
    nums = list(range(1, n + 1))
    
    for i in range(n, 0, -1):
        index = (k-1)//factorial[i-1]
        answer.append(nums[index])
        nums.pop(index)
        k %= factorial[i-1]
    return answer