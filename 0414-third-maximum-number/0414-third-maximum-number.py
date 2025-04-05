class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums)) #make unique 
        if len(nums) < 3:
            return max(nums)
        else:
            n = sorted(nums)
            return n[-3]
        