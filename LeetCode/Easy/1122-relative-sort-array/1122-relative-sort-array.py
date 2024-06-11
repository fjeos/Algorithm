class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import defaultdict
        
        arr1.sort()
        count = defaultdict(int)
        for num in arr1:
            count[num] += 1
        
        result = []
        for num in arr2:
            for i in range(count[num]):
                result.append(num)
                count[num] -= 1
        
        for key, value in filter(lambda x: x[1] > 0, count.items()):
           for _ in range(value):
            result.append(key)
            count[key] -= 1
            
        return result