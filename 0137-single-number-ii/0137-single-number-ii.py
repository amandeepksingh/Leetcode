from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]  #approach 1
        # approach 2 - dict with counts?
        # approach 3 - 2 sets 
        # complete_set = set(nums)
        # seen_set = set()
        # for n in nums:
        #     if n in seen_set:

