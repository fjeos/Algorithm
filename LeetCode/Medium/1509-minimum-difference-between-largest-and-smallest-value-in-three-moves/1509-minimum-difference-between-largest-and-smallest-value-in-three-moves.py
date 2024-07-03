class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        else:
            nums.sort()
            result = []

            i = 0
            j = -3
            while j < 0:
                result.append(nums[i:j][-1] - nums[i:j][0])
                i += 1
                j += 1
            result.append(nums[i:][-1] - nums[i:][0])
            return min(result)