class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별, 투포인터 확장
        def window(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, window(i, i + 1), window(i, i + 2), key=len)

        return result