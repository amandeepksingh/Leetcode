from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2) and set(word1) == set(word2): 
            c1 = Counter(word1)
            c2 = Counter(word2)
            print(list(c1.values()))
            print(list(c2.values()))
            if sorted(list(c1.values())) == sorted(list(c2.values())):
                return True
        return False
        
        