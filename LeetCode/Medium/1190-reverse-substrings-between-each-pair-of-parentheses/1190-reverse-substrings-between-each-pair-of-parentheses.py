class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        queue = deque()
        result = []
        
        for char in s:
            if char == "(":
                queue.append(len(result))
            elif char == ")":
                start = queue.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(char)
                
        return ''.join(result)