class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        set1 = set(nums1)
        set2 = set(nums2)
        
        set_result = set1 & set2
        
        for num in set_result:
            count = min(nums1.count(num), nums2.count(num))
            for _ in range(count):
                result.append(num)
            
        return result