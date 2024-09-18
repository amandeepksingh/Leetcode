class Solution:
    def isPalindrome(self, x: int) -> bool:
        x2 = 0
        x_copy = x
        while x > 0:
            x2 = x2*10 + x%10
            x = x//10
        return x2 == x_copy

        