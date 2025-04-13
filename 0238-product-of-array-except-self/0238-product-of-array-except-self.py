class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answers = [1]*len(nums)
        before = [1]*len(nums)
        after = [1]*len(nums)

        for i in range(1, len(nums)):
            before[i] = before[i-1]*nums[i-1]

        for i in range(2, len(nums) + 1):
            # print(nums[len(nums) - i])
            after[len(nums) - i] = after[len(nums) - i + 1]*nums[len(nums) - i + 1]

        # print(before)
        # print(after)
        return [after[i]*before[i] for i in range(len(nums))]




