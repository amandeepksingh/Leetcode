class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        max_len = 0
        for i in range(len(s)):
            subset = set()
            for j in range(i, len(s)):
                if s[j] in subset:
                    continue
                subset.add(s[j])
                sub = s[i:j+1]
                if len(sub) > max_len and len(set(sub)) == len(sub):
                    max_len = len(sub)
        return max_len
        