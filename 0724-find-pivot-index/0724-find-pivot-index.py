class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presums = [0]*len(nums)
        postsums = [0]*len(nums)
        if sum(nums[1:]) == 0:
            return 0
        for i in range(1, len(nums)):
            # presums[0] = 0
            # postsums[-1] = 0
            presums[i] = presums[i-1] + nums[i-1]
            postsums[len(nums)-1-i] = postsums[len(nums)-i] + nums[len(nums)-i]
        print(postsums)
        print(presums) 
        for i in range(len(nums)):
            if presums[i] == postsums[i]:
                return i
        return -1 