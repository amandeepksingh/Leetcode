class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        distset = set()
        while n > 0:
            minno = min(nums)
            maxno = max(nums)
            avg = (minno + maxno)/2
            distset.add(avg)
            nums.pop(0)
            nums.pop(-1)
            n = n -2 
        return len(distset)
        