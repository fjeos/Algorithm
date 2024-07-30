class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = list(str(x))
        is_pal = True
        if len(palindrome) != 1:
            for i in range(int(len(palindrome) // 2)):
                if palindrome[i] != palindrome[-i - 1]:
                    is_pal = False
                    break
                    
        return is_pal