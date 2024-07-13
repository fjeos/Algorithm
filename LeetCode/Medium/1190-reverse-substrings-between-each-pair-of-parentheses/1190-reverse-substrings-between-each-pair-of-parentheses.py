class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        queue = deque()
        s = list(s)

        for i in range(len(s)):
            if s[i] == "(":
                queue.append(i+1)
            elif s[i] == ")":
                start = queue.pop()
                s[start:i] = s[i-1:start-1:-1]

        return "".join(s).replace("(","").replace(")", "")