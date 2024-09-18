class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] == val:
                c = c + 1
                nums[i] = max(nums) + 1

        nums.sort()
        return len(nums) - c
            
