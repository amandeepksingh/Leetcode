class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # approach 1 
        k = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[k] = nums[i]
                seen.add(nums[i])
                k = k + 1
        # approach 2 - use collections counter and remove anything with a count greater than 1
        return k

                