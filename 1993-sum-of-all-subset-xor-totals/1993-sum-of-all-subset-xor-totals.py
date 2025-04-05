from itertools import chain, combinations

class Solution:
    @staticmethod
    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0 
        subs = self.powerset(nums)
        for p in list(subs):
            if len(p) == 1:
                total = total + p[0]
            elif len(p) > 1:
                output = p[0]
                for k in range(1, len(p)):
                    output = p[k]^output
                total = total + output
        return total
        