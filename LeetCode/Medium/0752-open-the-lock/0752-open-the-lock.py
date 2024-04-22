class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        visited = set(deadends)
        
        if "0000" not in visited:
            visited.add("0000")
            queue.append(("0000", 0))
            
        while queue:
            digits, moves = queue.popleft()
            if digits == target:
                return moves
            
            for i in range(4):
                next_num = digits[:i] + str((int(digits[i])+1)%10) + digits[i+1:]
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, moves + 1))
                    
                next_num = digits[:i] + str((int(digits[i])-1)%10) + digits[i+1:]
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, moves + 1))
                    
        return -1