class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # answer = dict()
        # answer[1] = set()
        # answer[2] = set()
        # for n in nums1:
        #     if n not in nums2:
        #         answer[1].add(n)
        # for n in nums2:
        #     if n not in nums1:
        #         answer[2].add(n)
        # # print(answer)
        # return [list(answer[1]), list(answer[2])]

        nums1set = set(nums1)
        nums2set = set(nums2)
        return [list(nums1set.difference(nums2set)), list(nums2set.difference(nums1set))]

        