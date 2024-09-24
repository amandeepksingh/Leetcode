class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) != len(set(nums)):
            for i in range(len(nums)):
                for j in range(i, min(len(nums), i + k + 1)):
                    if i !=j and nums[i] == nums[j] and abs(i-j) <= k:
                        return True 
        return False