import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)

        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True