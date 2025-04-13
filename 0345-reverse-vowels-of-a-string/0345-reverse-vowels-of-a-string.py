class Solution:
    def reverseVowels(self, s: str) -> str:
        # 2 pointer approach
        p1 = 0 
        p2 = len(s) - 1
        s = list(s)
        while p1 < p2:
            if s[p1] in set('AEIOUaeiou') and s[p2] in set('AEIOUaeiou'):
                print(s[p1])
                temp = s[p1]
                s[p1] = s[p2]
                s[p2] = temp
                p1 = p1 + 1
                p2 = p2 - 1
            if s[p1] not in set('AEIOUaeiou'):
                p1 = p1 + 1
            if s[p2] not in set('AEIOUaeiou'):
                p2 = p2 - 1
        return "".join(c for c in s)
