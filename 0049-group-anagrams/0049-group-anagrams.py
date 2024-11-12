class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_dict = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in an_dict.keys():
                an_dict[sorted_s].append(s)
            else:
                an_dict[sorted_s] = [s]
        return list(an_dict.values())
