class Solution:
    def isPalindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        # brute force 
        for length in range(len(s), 0, -1):
                    for start in range(len(s) - length + 1):
                        if self.isPalindrome(s[start: start + length]):
                            return s[start : start + length]
            




    
        