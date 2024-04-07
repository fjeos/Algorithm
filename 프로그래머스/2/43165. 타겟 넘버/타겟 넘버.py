from collections import deque, defaultdict
def solution(numbers, target):
    index = value = 0
    
    def dfs(nums, target, value, index):
        if index == len(nums):
            return 1 if value == target else 0
        return dfs(nums, target, value + nums[index], index + 1) \
                + dfs(nums, target, value - nums[index], index + 1)
    
    answer = dfs(numbers, target, index, value)
    return answer