class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        if len(nums) > 1:
            for n in range(0, len(nums)-1, 2):
                print(nums[n], nums[n+1])
                if nums[n] != nums[n+1]:
                    return nums[n]
            return nums[-1]
        else:
            return nums[0]
        