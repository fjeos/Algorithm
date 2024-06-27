class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        n = len(edges)
        count = defaultdict(int)
        for edge in edges:
            count[edge[0]] += 1
            count[edge[1]] += 1

        for key, value in count.items():
            if value == n:
                return key
        