from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_dict = {}
        # for num in nums:
        #     freq_dict[num] = freq_dict.get(num, 0) + 1
        # for key, value in freq_dict.items():
        #     if value > len(nums)/2:
        #         return key
        return Counter(nums).most_common()[0][0]
        