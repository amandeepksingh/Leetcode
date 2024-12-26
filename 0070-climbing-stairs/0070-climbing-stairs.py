class Solution:
    # dynamic programming approach 
    # either take 1 or take 2 at each step 

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        c = [1, 2] 
        while (len(c) < n):
            c.append(c[-1] + c[-2])
            print(c)
        return c[-1]
        