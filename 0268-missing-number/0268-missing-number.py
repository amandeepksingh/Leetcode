class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        num_max = max(num_set)
        if len(num_set) == num_max+1:
            return num_max + 1
        for i in range(num_max):
            if i not in num_set:
                return i
        return num_max+1
        