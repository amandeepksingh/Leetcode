# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1 
        h = n 
        while l < h:
            m = (l + h)//2
            # print(l, m, h, guess(m))
            if guess(m) == 0:
                return m 
            if guess(m) > 0: 
                l = m + 1
            if guess(m) < 0:
                h = m - 1
        return l

        