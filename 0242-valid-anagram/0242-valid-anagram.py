from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) == set(t):
           if Counter(s) == Counter(t):
            return True 
        return False
        