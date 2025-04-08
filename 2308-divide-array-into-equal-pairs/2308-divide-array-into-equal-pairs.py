from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            l = Counter(nums)
            for n in l.values():
                if n % 2 != 0:
                    return False
            return True 
        return False 
        