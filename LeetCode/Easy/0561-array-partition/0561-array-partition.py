class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2
        result, i = 0, 0
        for _ in range(n):
            result += min(nums[i], nums[i+1])
            i += 2
        return result