def solution(n, k):
    answer = []
    facto = [1, 1]
    for i in range(2, n + 1):
        facto.append(facto[i-1] * i)
    nums = list(range(1, n + 1))
    k -= 1
    while k > 0:
        index = k // facto[n-1]
        answer.append(nums[index])
        nums.pop(index)
        k %= facto[n-1]
        n -= 1
    answer += nums
    
    return answer