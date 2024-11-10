from collections import Counter 
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) == len(arr):
            return Counter(target) == Counter(arr)
            