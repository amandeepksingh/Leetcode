class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(i, len(haystack)+1):
                substr = haystack[i:j]
                if substr == needle or haystack == needle:
                    return i 
        return -1