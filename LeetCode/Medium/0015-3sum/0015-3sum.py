class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        dic = defaultdict(int)
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    if dic[str(temp)] == 0:
                        dic[str(temp)] = 1
                        answer.append(temp)
                    left += 1
                    right -= 1
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
                
        return answer