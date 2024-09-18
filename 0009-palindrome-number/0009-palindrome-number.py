class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if (x < 10):
            return True 
        d = x
        px = x%10
        x = x//10
        while (x > 0):
            px = px*10 + x%10
            x = x//10
        return d == px 
        