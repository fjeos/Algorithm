class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        result = sorted([-num if num < 0 else num for num in nums if -num in nums], reverse = True)
        return result[0] if result else -1