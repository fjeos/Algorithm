class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        answer = -1
        for num in nums:
            if -num in nums:
                if answer < num:
                    answer = -num if num < 0 else num
        return answer
        