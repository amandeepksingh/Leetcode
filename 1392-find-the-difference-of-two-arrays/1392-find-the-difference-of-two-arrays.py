class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = dict()
        answer[1] = set()
        answer[2] = set()
        for n in nums1:
            if n not in nums2:
                answer[1].add(n)
        for n in nums2:
            if n not in nums1:
                answer[2].add(n)
        print(answer)
        return [list(answer[1]), list(answer[2])]

        