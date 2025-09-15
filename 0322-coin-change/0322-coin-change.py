class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp  = [amount + 1] * (amount + 1)
        dp[0] = 0 # 0 coins needed for amt = 0 

        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x-c] + 1)
        
        return dp[amount] if dp[amount] != amount +1 else -1

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memo = {}
    #     def dfs(rem):
    #         if rem == 0: return 0
    #         if rem < 0: return float('inf')
    #         if rem in memo: return memo[rem]
    #         else:
    #             min_coins = float('inf')
    #             for c in coins:
    #                 res = dfs(rem-c)
    #                 if res != float('inf'):
    #                     min_coins = min(min_coins, res + 1)
    #             memo[rem] = min_coins
    #             return min_coins

    #     ans = dfs(amount)
    #     return ans if ans != float('inf') else -1 
