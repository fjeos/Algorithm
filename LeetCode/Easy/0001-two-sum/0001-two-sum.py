class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, 1
        while left < len(nums) - 1:
            if right == len(nums):
                left += 1
                right = left + 1
                continue
            if nums[left] + nums[right] == target:
                return [left, right]
            right += 1