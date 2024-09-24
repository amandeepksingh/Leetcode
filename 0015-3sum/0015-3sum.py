class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target, arr):
            mappy = {}
            outputi = []
            for i in arr:
                if target - i not in mappy and i not in mappy:
                    mappy[i] = 0
                elif target - i in mappy and mappy[target - i] == 0:
                    mappy[target - i] += 1
                    outputi.append([i, target - i, -1*target])
            return outputi

        output = []
        nums = sorted(nums)
        completed_targets = set()
        for i in range(len(nums)):
            if nums[i] not in completed_targets:
                completed_targets.add(nums[i])
                output += twoSum(-1*nums[i], nums[i+1:])
        return output 