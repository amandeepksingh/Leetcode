class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # potions = sorted(potions)
        # pairs = [0]*len(spells)
        # for i in range(len(spells)):
        #     # print("i",i)
        #     m = len(potions)//2
        #     l = 0 
        #     h = len(potions)
        #     if spells[i]*potions[m] < success:
        #         l = m + 1 
        #         h = len(potions)
        #     for j in range(l, h):
        #         # print("j", j)
        #         if spells[i]*potions[j] >= success:
        #             pairs[i] = pairs[i] + len(potions) - j 
        #             # print("breaking @", j)
        #             break
        # return pairs 

        potions = sorted(potions)
        pairs = [0]*len(spells)
        for i in range(len(spells)):
            # print("i",i)
            l = 0 
            h = len(potions) - 1 
            while l <= h:
                m = (l+h)// 2 
                if spells[i]*potions[m] < success: 
                    l = m + 1 
                else:
                    h = m - 1
            pairs[i] = len(potions) - l 
        return pairs 