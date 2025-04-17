class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) >= 3:  
            if sorted(nums) == nums:
                return True 
            for i in range(1, len(nums)):
                if min(nums[:i]) < nums[i] and nums[i] < max(nums[i:]):
                    return True 
        return False 