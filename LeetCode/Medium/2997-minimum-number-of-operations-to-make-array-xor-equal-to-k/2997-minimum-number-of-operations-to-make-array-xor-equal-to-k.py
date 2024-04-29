class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_xor = 0
        for i in range(len(nums)):
            final_xor = final_xor ^ nums[i]
        
        result = final_xor ^ k
        count = 0
        while result > 0:
            count += 1
            result = result & (result-1)
        
        return count
