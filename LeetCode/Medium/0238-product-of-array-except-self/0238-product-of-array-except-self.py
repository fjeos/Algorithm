class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for i in range(1, len(nums)):
            result.append(result[-1] * nums[i-1])

        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * p
            p *= nums[i]

        return result