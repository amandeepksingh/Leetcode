# # houses in a circle 
# # first and last will be neighbors 
# # adjacent houses have a connected security system - so cannot do adjacent houses 
# # nums[i] = money @ house # i 
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def house_robber_1(nums):
#             dp = [0] * len(nums) # what exactly does dp represent here?
#             dp[0] = nums[0]
#             dp[1] = max(nums[0], nums[1])
#             for i in range(2, len(nums)):
#                 dp[i] = max(nums[i] + dp[i-2], dp[i-1])
#             return dp[-1]
                 
#         if len(nums) == 0:
#             return 0 
#         if len(nums) <= 3: # if there are only two houses we go to the one w more money 
#             return max(nums)

#         return max(house_robber_1(nums[:-1]), house_robber_1(nums[1:]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[1], dp[0])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return dp[-1]
        
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))

        
        
        