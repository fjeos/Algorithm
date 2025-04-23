def solution(numbers, target):
    answer = 0
    def dfs(depth, now_sum):
        nonlocal answer
        if depth == len(numbers):
            if now_sum == target:
                answer += 1
            return
        dfs(depth + 1, now_sum + numbers[depth])
        dfs(depth + 1, now_sum - numbers[depth])
    dfs(0, 0)
        
    return answer