class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_max = max(nums)
        if len(nums) == num_max+1:
            return num_max + 1
        num_set = set(nums)
        for i in range(num_max):
            if i not in num_set:
                return i
        return num_max+1
        