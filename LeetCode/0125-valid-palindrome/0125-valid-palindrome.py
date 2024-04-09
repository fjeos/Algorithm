class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^0-9a-z]", "", s)
        return s == s[::-1]


        