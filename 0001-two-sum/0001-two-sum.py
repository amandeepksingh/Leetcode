class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force 
        num_set = set(nums)
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                return [i, nums.index(target - nums[i])]



















        # # seen = {}
        
        # # for i in range(len(nums)):
        # #     comp = target - nums[i]
        # #     if comp in seen:
        # #         print(comp)
        # #         return [i, seen[comp]]
        # #     seen[nums[i]] = i

        # for i in range(len(nums)):
        #     if target - nums[i] in nums and i != nums.index(target - nums[i]):
        #         return [i, nums.index(target - nums[i])]